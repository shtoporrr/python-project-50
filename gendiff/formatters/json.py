import json


def format_diff(diff):
    """Format diff tree in JSON format."""
    return json.dumps(diff, indent=2)
