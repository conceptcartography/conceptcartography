import csv
import os
import re
import yaml
from collections import defaultdict

def parse_definitions(def_str):
    return [s.strip() for s in def_str.split('//') if s.strip()]

def format_definition_text(definition, reference_lookup, used_refs):
    # Turn citation-like things into markdown links if found in ref lookup
    def replace_citation(match):
        citation = match.group(1).strip()
        slug = slugify(citation)
        if slug in reference_lookup:
            used_refs.add(slug)
            return f"[{citation}](#ref-{slug})"
        return citation  # leave it unlinked if not found
    return re.sub(r"[\(\[]([^()\[\]]+)[\)\]]", replace_citation, definition)

def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

def remove_square_brackets(text):
    return text.replace('[', '').replace(']', '')

def extract_year(text):
    match = re.search(r"[\(\[]?(19|20)\d{2}[\)\]]?", text)
    return match.group(0).strip("()[]") if match else ""

def parse_examples(example_str):
    parts = [s.strip() for s in example_str.split(';') if s.strip()]
    return [{"description": p, "year": extract_year(p)} for p in parts]

def clean_reference_blocks(raw_refs):
    cleaned_refs = []
    buffer = ""

    for ref in raw_refs:
        ref = ref.strip()
        if not ref:
            continue

        # If it's just a URL fragment like 'https:' or 'doi:', skip
        if re.fullmatch(r'https?:', ref.lower()) or re.fullmatch(r'doi:', ref.lower()):
            continue

        # If it's a URL/DOI starting with no context, add to previous line
        if (ref.startswith("http") or ref.startswith("doi:") or ref.startswith("doi.org")) and buffer:
            buffer += " " + ref
        else:
            if buffer:
                cleaned_refs.append(buffer)
            buffer = ref

    if buffer:
        cleaned_refs.append(buffer)

    return cleaned_refs


def parse_relations(relation_str):
    if not relation_str:
        return []
    relation_items = []
    parts = [r.strip() for r in relation_str.split(';') if r.strip()]
    for part in parts:
        match = re.match(r"\((.*?)\)\s*(.+)", part)
        if match:
            relation_items.append({
                "type": match.group(1).strip().lower(),
                "target": match.group(2).strip().lower()
            })
        else:
            tokens = part.split(None, 1)
            if len(tokens) == 2:
                relation_items.append({
                    "type": tokens[0].strip().lower(),
                    "target": tokens[1].strip().lower()
                })
            else:
                print(f"⚠️ Skipping unrecognized relation format: '{part}'")
    return relation_items



# First pass: collect all concept data and relations
concepts = {}
reverse_relations = defaultdict(list)

with open("map-data/concepts-final.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        concept = row["concept"].strip().lower()
        relations = parse_relations(row["relations"])
        concepts[concept] = {
            "slug": slugify(concept),
            "concept": concept,
            "references": [row["reference"].strip()],
            "definitions": parse_definitions(row["definitions"]),
            "examples": parse_examples(row["examples"]),
            "relations": relations
        }

        # Build reverse relation map
        for rel in relations:
            reverse_relations[rel["target"]].append({
                "type": rel["type"],
                "target": concept
            })

# Merge reverse relations
for concept, data in concepts.items():
    path = f"docs/concepts/{data['slug']}.md"
    os.makedirs(os.path.dirname(path), exist_ok=True)

    # Parse and sort unique references
    # Parse and sort unique references
    ref_list = []
    for ref_str in data["references"]:
        ref_list += [r.strip() for r in ref_str.split("//") if r.strip()]

    # Clean up multi-line references
    ref_list = clean_reference_blocks(ref_list)
    ref_list = sorted(set(ref_list), key=str.lower)


    with open(path, "w", encoding="utf-8") as f:
        f.write("---\n")
        cleaned_definitions = [remove_square_brackets(d) for d in data["definitions"]]

        cleaned_examples = [
            {"description": remove_square_brackets(e["description"])}
            for e in data["examples"]
        ]

        yaml.dump({
            "concept": data["concept"],
            "references": ref_list,
            "definitions": cleaned_definitions,
            "examples": cleaned_examples,
            "relations": data["relations"]
        }, f, sort_keys=False, allow_unicode=True)

        f.write("---\n\n")

        f.write(f"# {data['concept']}\n\n")

        # Definitions as blockquotes
        if data["definitions"]:
            f.write("## 📖 Definitions\n\n")
            for d in cleaned_definitions:
                f.write(f"> {d}\n\n")


        # Examples
        if data["examples"]:
            f.write("## 💡 Examples\n\n")
            for e in cleaned_examples:
                f.write(f"- {e['description']}\n")
            f.write("\n")

        # Relations
        if data["relations"]:
            f.write("## 🔗 Relations\n\n")
            for r in data["relations"]:
                target_slug = slugify(r["target"])
                f.write(f"- **{r['type']}**: [{r['target']}](./{target_slug}.md)\n")
            f.write("\n")

        # References
        if ref_list:
            f.write("## 📚 References\n\n")
            for ref in ref_list:
                    # Convert any URL in the reference to a clickable Markdown link
                def linkify_reference(ref):
                    # Linkify DOI only if not already inside a markdown link
                    ref = re.sub(r'\bdoi: *([^\s\)\]]+)', r'[doi:\1](https://doi.org/\1)', ref)

                    # Fix raw URLs (not already in markdown)
                    def url_replacer(match):
                        url = match.group(0)
                        return f'<{url}>'

                    ref = re.sub(r'(?<![\[\(])https?://[^\s\)\]]+', url_replacer, ref)
                    return ref



                f.write(f"- {linkify_reference(ref)}\n")      
                        # Giscus comments
                f.write('\n---\n\n')
                f.write("""<script src="https://giscus.app/client.js"
                data-repo="natesheehan/conceptcartography"
                data-repo-id="R_kgDOPB5QiQ"
                data-category="General"
                data-category-id="DIC_kwDOPB5Qic4CsAxd"
                data-mapping="pathname"
                data-strict="0"
                data-reactions-enabled="1"
                data-emit-metadata="0"
                data-input-position="bottom"
                data-theme="catppuccin_mocha"
                data-lang="en"
                crossorigin="anonymous"
                async>
        </script>
        """)
  
