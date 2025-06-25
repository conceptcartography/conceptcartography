import csv
import os
import re
import yaml

def parse_definitions(def_str):
    return [s.strip() for s in def_str.split('//') if s.strip()]

def extract_year(text):
    # Search for year pattern: (2023), [2023], or just 4-digit year
    match = re.search(r"[\(\[]?(19|20)\d{2}[\)\]]?", text)
    return match.group(0).strip("()[]") if match else ""

def parse_examples(example_str):
    parts = [s.strip() for s in example_str.split(';') if s.strip()]
    return [{"description": p, "year": extract_year(p)} for p in parts]

def parse_relations(relation_str):
    relation_items = []
    pattern = r"\((.*?)\)\s*([^;]+)"
    for match in re.finditer(pattern, relation_str):
        relation_items.append({
            "type": match.group(1).strip(),
            "target": match.group(2).strip()
        })
    return relation_items

def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

with open("concepts.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        concept = row["concept"].strip()
        slug = slugify(concept)
        path = f"docs/concepts/{slug}.md"

        data = {
            "concept": concept,
            "references": [row["reference"].strip()],
            "definitions": parse_definitions(row["definitions"]),
            "examples": parse_examples(row["examples"]),
            "relations": parse_relations(row["relations"])
        }

        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write("---\n")
            yaml.dump(data, f, sort_keys=False, allow_unicode=True)
            f.write("---\n\n")
            f.write(f"# 🧠 {concept}\n\n")

            # Definitions as quotes
            if data["definitions"]:
                f.write("## 📖 Definitions\n\n")
                for d in data["definitions"]:
                    f.write(f"> {d}\n\n")

            # Examples with year bolded
            if data["examples"]:
                f.write("## 💡 Examples\n\n")
                for e in data["examples"]:
                    year_str = f"**{e['year']}** — " if e["year"] else ""
                    f.write(f"- {year_str}{e['description']}\n")
                f.write("\n")

            # Relations with links
            if data["relations"]:
                f.write("## 🔗 Relations\n\n")
                for r in data["relations"]:
                    slug = slugify(r["target"])
                    f.write(f"- **{r['type']}**: [{r['target']}](./{slug}.md)\n")
                f.write("\n")

            # References: autodetect links if present
            if data["references"]:
                f.write("## 📚 References\n\n")
                for ref in data["references"]:
                    if "http" in ref:
                        f.write(f"- [{ref}]({ref})\n")
                    else:
                        f.write(f"- {ref}\n")

            # Add Giscus comment widget
            f.write("\n\n---\n\n")
            f.write(
                '<script src="https://giscus.app/client.js"\n'
                '        data-repo="natesheehan/conceptcartography"\n'
                '        data-repo-id="R_kgDOPB5QiQ"\n'
                '        data-category="General"\n'
                '        data-category-id="DIC_kwDOPB5Qic4CsAxd"\n'
                '        data-mapping="pathname"\n'
                '        data-strict="0"\n'
                '        data-reactions-enabled="1"\n'
                '        data-emit-metadata="0"\n'
                '        data-input-position="bottom"\n'
                '        data-theme="catppuccin_mocha"\n'
                '        data-lang="en"\n'
                '        crossorigin="anonymous"\n'
                '        async>\n</script>\n'
            )
