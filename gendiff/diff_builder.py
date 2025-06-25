def build_diff(data1, data2):
    """Build internal diff representation."""
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []

    for key in all_keys:
        if key not in data1:
            # Key was added
            diff.append({
                'key': key,
                'type': 'added',
                'value': data2[key]
            })
        elif key not in data2:
            # Key was removed
            diff.append({
                'key': key,
                'type': 'removed',
                'value': data1[key]
            })
        elif data1[key] == data2[key]:
            # Key unchanged
            diff.append({
                'key': key,
                'type': 'unchanged',
                'value': data1[key]
            })
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            # Both values are dicts - recurse
            diff.append({
                'key': key,
                'type': 'nested',
                'children': build_diff(data1[key], data2[key])
            })
        else:
            # Key was changed
            diff.append({
                'key': key,
                'type': 'changed',
                'old_value': data1[key],
                'new_value': data2[key]
            })

    return diff
