import os
import csv
import json
import re

data_dir = "map-data"
output_dir = "docs/maps"
names_registry_path = os.path.join(output_dir, "names.json")

symmetric_relations = {"equivalent to", "similar to", "counteracts"}

def slugify(text):
    return re.sub(r'[^\w\-]', '', text.lower().replace(" ", "-")).strip("-")

def title_case_first(s):
    return s[:1].upper() + s[1:] if s else ""

def parse_relations(relation_str):
    if not relation_str:
        return []
    rels = [r.strip() for r in relation_str.split(";") if r.strip()]
    results = []
    for r in rels:
        match = re.match(r"\((.*?)\)\s*(.+)", r)
        if match:
            rel_type = match.group(1).strip().lower()
            target = match.group(2).strip()
            results.append((rel_type, target))
    return results

# Load slug registry
slug_registry = {}
if os.path.exists(names_registry_path):
    with open(names_registry_path, "r", encoding="utf-8") as f:
        slug_registry = json.load(f)

for filename in os.listdir(data_dir):
    if filename.endswith("-metadata.csv"):
        base = filename.replace("-metadata.csv", "")
        metadata_file = os.path.join(data_dir, filename)
        csv_file = os.path.join(data_dir, f"{base}-map.csv")

        if not os.path.exists(csv_file):
            print(f"⚠ Missing map file for {base}")
            continue

        # Read metadata CSV (all rows)
        metadata_entries = []
        with open(metadata_file, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            metadata_entries = list(reader)

        title = title_case_first(metadata_entries[0].get("title", base).strip())
        authors = metadata_entries[0].get("authors", "").strip()
        description = metadata_entries[0].get("description", "").strip()

        # Generate unique slug
        raw_slug = slugify(title)
        slug = raw_slug
        count = 1
        while slug in slug_registry.values():
            slug = f"{raw_slug}-{count}"
            count += 1
        slug_registry[title] = slug

        # Parse concept CSV and extract nodes/edges
        nodes = set()
        edges = []
        with open(csv_file, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                source = row["concept"].strip()
                nodes.add(source)
                for rel_type, target in parse_relations(row.get("relations", "")):
                    nodes.add(target)
                    edges.append({
                        "source": source,
                        "target": target,
                        "type": rel_type
                    })
                    if rel_type in symmetric_relations and source != target:
                        edges.append({
                            "source": target,
                            "target": source,
                            "type": rel_type
                        })

        # Write graph JSON
        with open(os.path.join(output_dir, f"{slug}.json"), "w", encoding="utf-8") as f:
            json.dump({
                "nodes": [{"id": n} for n in sorted(nodes)],
                "links": edges
            }, f, indent=2, ensure_ascii=False)

        # Write Markdown + HTML/JS graph
        with open(os.path.join(output_dir, f"{slug}.md"), "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n")
            if authors:
                f.write("## ✍️ Authors\n")
                f.write(f"{authors}\n\n")

            if description:
                f.write("## ❔ Description\n")
                f.write(f"{description}\n\n")

            f.write("<!-- GRAPH START -->\n")
            with open("graph.html", "r", encoding="utf-8") as tpl:
                html = tpl.read().replace("../../assets/graph.json", f"{slug}.json")
                f.write(html)
            f.write("<!-- GRAPH END -->\n")

# Save updated slug registry
with open(names_registry_path, "w", encoding="utf-8") as f:
    json.dump(slug_registry, f, indent=2)

print("✔ Maps built and saved in docs/maps/")
