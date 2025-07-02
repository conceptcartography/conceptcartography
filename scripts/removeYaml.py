import os
import re

def remove_yaml_headers_from_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".md"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Remove YAML header (--- at start and end)
            new_content = re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, flags=re.DOTALL)

            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

            print(f"Processed: {filename}")

# Replace this with your actual folder path
folder = "docs/concepts/"
remove_yaml_headers_from_folder(folder)
