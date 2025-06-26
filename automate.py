import csv
import os
import re
import yaml
from collections import defaultdict

def parse_definitions(def_str):
    return [s.strip() for s in def_str.split('//') if s.strip()]

def extract_year(text):
    match = re.search(r"[\(\[]?(19|20)\d{2}[\)\]]?", text)
    return match.group(0).strip("()[]") if match else ""

def parse_examples(example_str):
    parts = [s.strip() for s in example_str.split(';') if s.strip()]
    return [{"description": p, "year": extract_year(p)} for p in parts]

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

def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

# First pass: collect all concept data and relations
concepts = {}
reverse_relations = defaultdict(list)

with open("dict.csv", newline='', encoding='utf-8') as csvfile:
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
    incoming = reverse_relations.get(concept, [])
    all_relations = data["relations"] + incoming
    # Remove duplicates
    seen = set()
    data["relations"] = [
        r for r in all_relations
        if (r["type"], r["target"]) not in seen and not seen.add((r["type"], r["target"]))
    ]

# Write Markdown files
for concept, data in concepts.items():
    path = f"docs/concepts/{data['slug']}.md"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write("---\n")
        yaml.dump({
            "concept": data["concept"],
            "references": data["references"],
            "definitions": data["definitions"],
            "examples": data["examples"],
            "relations": data["relations"]
        }, f, sort_keys=False, allow_unicode=True)
        f.write("---\n\n")

        f.write(f"# {data['concept']}\n\n")

        if data["definitions"]:
            f.write("## 📖 Definitions\n\n")
            for d in data["definitions"]:
                f.write(f"- {d}\n")
            f.write("\n")

        if data["examples"]:
            f.write("## 💡 Examples\n\n")
            for e in data["examples"]:
                year_str = f"**{e['year']}** — " if e["year"] else ""
                f.write(f"- {year_str}{e['description']}\n")
            f.write("\n")

        if data["relations"]:
            f.write("## 🔗 Relations\n\n")
            for r in data["relations"]:
                target_slug = slugify(r["target"])
                f.write(f"- **{r['type']}**: [{r['target']}](./{target_slug}.md)\n")
            f.write("\n")

        if data["references"]:
            f.write("## 📚 References\n\n")
            for ref in data["references"]:
                f.write(f"- {ref}\n")
