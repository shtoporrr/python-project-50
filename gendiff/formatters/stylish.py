def format_value(value, depth):
    """Format value for output with proper indentation."""
    if isinstance(value, dict):
        indent = '    ' * (depth + 1)
        close_indent = '    ' * depth
        lines = []
        for key, val in value.items():
            lines.append(f"{indent}{key}: {format_value(val, depth + 1)}")
        return "{\n" + "\n".join(lines) + "\n" + close_indent + "}"
    elif value is None:
        return "null"
    elif isinstance(value, bool):
        return "true" if value else "false"
    elif isinstance(value, str) and value == "":
        return ""
    else:
        return str(value)


def format_node(node, indent, depth):
    """Format a single diff node."""
    key = node['key']
    node_type = node['type']

    if node_type == 'added':
        value = format_value(node['value'], depth + 1)
        return f"{indent}  + {key}: {value}"
    elif node_type == 'removed':
        value = format_value(node['value'], depth + 1)
        return f"{indent}  - {key}: {value}"
    elif node_type == 'unchanged':
        value = format_value(node['value'], depth + 1)
        return f"{indent}    {key}: {value}"
    elif node_type == 'changed':
        old_value = format_value(node['old_value'], depth + 1)
        new_value = format_value(node['new_value'], depth + 1)
        return [f"{indent}  - {key}: {old_value}",
                f"{indent}  + {key}: {new_value}"]
    elif node_type == 'nested':
        nested_diff = format_diff(node['children'], depth + 1)
        return f"{indent}    {key}: {nested_diff}"
    else:
        raise ValueError(f"Unknown node type: {node_type}")


def format_diff(diff, depth=0):
    """Format diff tree in stylish format."""
    if not diff:
        return "{}"

    lines = []
    indent = '    ' * depth

    for node in diff:
        formatted = format_node(node, indent, depth)
        if isinstance(formatted, list):
            lines.extend(formatted)
        else:
            lines.append(formatted)

    close_indent = '    ' * depth
    return "{\n" + "\n".join(lines) + "\n" + close_indent + "}"
