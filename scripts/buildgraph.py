import os
import json
import re

concept_dir = "docs/concepts"
output_path = "docs/assets/graph.json"

nodes = {}
edges = []

symmetric_relations = {"equivalent to", "similar to", "counteracts"}

def parse_markdown_lines(filepath):
    concept = None
    definition_lines = []
    relations = []
    references = []
    in_definitions = False
    in_references = False

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()

            # Get concept name (first H1)
            if stripped.startswith("# ") and not concept:
                concept = stripped[2:].strip()

            # Detect sections
            if stripped.lower().startswith("##") and "definition" in stripped.lower():
                in_definitions = True
                in_references = False
                continue
            if stripped.lower().startswith("##") and "reference" in stripped.lower():
                in_references = True
                in_definitions = False
                continue
            if stripped.lower().startswith("##"):
                # New section
                in_definitions = False
                in_references = False

            # Collect definitions (quotes or paragraphs)
            if in_definitions and (stripped.startswith(">") or stripped):
                definition_lines.append(stripped)

            # Collect references (markdown list items)
            if in_references and stripped.startswith("-"):
                references.append(stripped)

            # Collect relations (markdown list items)
            rel_match = re.match(r'- \*\*(.*?)\*\*:\s*\[(.*?)\]\(.*?\)', stripped)
            if rel_match:
                relations.append({
                    "type": rel_match.group(1).strip().lower(),
                    "target": rel_match.group(2).strip()
                })

    return {
        "concept": concept,
        "definition": "\n".join(definition_lines).strip(),
        "relations": relations,
        "reference": "\n".join(references).strip()
    }

# Step 1: Collect nodes
for filename in os.listdir(concept_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(concept_dir, filename)
        data = parse_markdown_lines(filepath)
        if not data["concept"]:
            print(f"⚠ Skipping {filename}: no concept found")
            continue

        concept_id = data["concept"].strip().lower()
        nodes[concept_id] = {
            "id": concept_id,
            "title": data["concept"].strip(),
            "definition": data["definition"],
            "reference": data["reference"],
            "filename": filename
        }

# Step 2: Collect edges
for concept_id, node_data in list(nodes.items()):
    filepath = os.path.join(concept_dir, node_data["filename"])
    data = parse_markdown_lines(filepath)
    for rel in data["relations"]:
        target = rel["target"].strip().lower()
        rel_type = rel["type"].strip().lower()
        if target and rel_type:
            edges.append({
                "source": concept_id,
                "target": target,
                "type": rel_type
            })
            if rel_type in symmetric_relations and concept_id != target:
                edges.append({
                    "source": target,
                    "target": concept_id,
                    "type": rel_type
                })
            if target not in nodes:
                nodes[target] = {
                    "id": target,
                    "title": target.title(),
                    "definition": "",
                    "reference": "",
                    "filename": ""  # No file
                }

# Final graph
graph = {
    "nodes": list(nodes.values()),
    "links": edges
}

os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, "w", encoding="utf-8") as out:
    json.dump(graph, out, indent=2, ensure_ascii=False)

print(f"✔ Graph built with {len(graph['nodes'])} nodes and {len(graph['links'])} edges.")
