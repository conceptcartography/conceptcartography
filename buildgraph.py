import os
import re
import json
import yaml

concept_dir = "docs/concepts"
output_path = "docs/assets/graph.json"

nodes = []
edges = []
concept_ids = set()

def extract_frontmatter(content):
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        return None
    frontmatter = match.group(1)
    return yaml.safe_load(frontmatter)

for filename in os.listdir(concept_dir):
    if filename.endswith(".md"):
        with open(os.path.join(concept_dir, filename), "r", encoding="utf-8") as f:
            content = f.read()
            data = extract_frontmatter(content)
            if not data or "concept" not in data:
                continue

            concept = data["concept"]
            concept_ids.add(concept)
            nodes.append({ "id": concept })

            for rel in data.get("relations", []):
                if rel.get("target") and rel.get("type"):
                    edges.append({
                        "source": concept,
                        "target": rel["target"],
                        "type": rel["type"]
                    })

# Optional: filter out orphan edges
edges = [e for e in edges if e["target"] in concept_ids]

graph = { "nodes": nodes, "links": edges }

os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, "w", encoding="utf-8") as out:
    json.dump(graph, out, indent=2, ensure_ascii=False)

print(f"✔ Graph built with {len(nodes)} nodes and {len(edges)} edges.")
