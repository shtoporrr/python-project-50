"""Plain formatter for diff output."""


def format_value(value):
    """Format value for plain output."""
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return 'true' if value else 'false'
    else:
        return str(value)


def format_diff(diff, path=''):
    """Format diff tree in plain format."""
    lines = []

    for node in diff:
        node_type = node['type']
        key = node['key']
        current_path = f"{path}.{key}" if path else key

        if node_type == 'added':
            value = format_value(node['value'])
            lines.append(
                f"Property '{current_path}' was added with value: {value}"
            )
        elif node_type == 'removed':
            lines.append(f"Property '{current_path}' was removed")
        elif node_type == 'changed':
            old_value = format_value(node['old_value'])
            new_value = format_value(node['new_value'])
            lines.append(
                f"Property '{current_path}' was updated. "
                f"From {old_value} to {new_value}"
            )
        elif node_type == 'nested':
            nested_lines = format_diff(node['children'], current_path)
            lines.extend(nested_lines)
        # unchanged nodes are not included in plain format

    return lines
