import os
import re
import json
import yaml

concept_dir = "docs/concepts"
output_path = "docs/assets/graph.json"

nodes = {}
edges = []

def extract_frontmatter(content):
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        return None
    frontmatter = match.group(1)
    return yaml.safe_load(frontmatter)

# Step 1: Collect all concept IDs (lowercased)
for filename in os.listdir(concept_dir):
    if filename.endswith(".md"):
        with open(os.path.join(concept_dir, filename), "r", encoding="utf-8") as f:
            content = f.read()
            data = extract_frontmatter(content)
            if not data or "concept" not in data:
                continue

            concept = data["concept"].strip().lower()
            nodes[concept] = True  # track unique concepts

# Step 2: Parse all relations
for filename in os.listdir(concept_dir):
    if filename.endswith(".md"):
        with open(os.path.join(concept_dir, filename), "r", encoding="utf-8") as f:
            content = f.read()
            data = extract_frontmatter(content)
            if not data or "concept" not in data:
                continue

            source = data["concept"].strip().lower()

            source = data["concept"].strip().lower()
            for rel in data.get("relations", []):
                target = rel.get("target", "").strip().lower()
                rel_type = rel.get("type", "").strip()
                if target and rel_type:
                    edges.append({
                        "source": source,
                        "target": target,
                        "type": rel_type
                    })
                    nodes[target] = True


# Final JSON structure
graph = {
    "nodes": [{"id": concept} for concept in sorted(nodes)],
    "links": edges
}

os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, "w", encoding="utf-8") as out:
    json.dump(graph, out, indent=2, ensure_ascii=False)

print(f"✔ Graph built with {len(graph['nodes'])} nodes and {len(graph['links'])} edges.")
