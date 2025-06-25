import json
import yaml
import os


def parse_file(file_path):
    """Parse file based on its extension."""
    _, ext = os.path.splitext(file_path)

    with open(file_path, 'r') as file:
        if ext.lower() in ['.json']:
            return json.load(file)
        elif ext.lower() in ['.yml', '.yaml']:
            return yaml.safe_load(file)
        else:
            raise ValueError(f"Unsupported file format: {ext}")
