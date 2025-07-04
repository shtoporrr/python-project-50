import argparse
from gendiff.parser import parse_file
from gendiff.diff_builder import build_diff
from gendiff.formatters.stylish import format_diff as format_stylish
from gendiff.formatters.plain import format_diff as format_plain
from gendiff.formatters.json import format_diff as format_json


def generate_diff(file_path1, file_path2, format_name='stylish'):
    """Generate diff between two files."""
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)

    diff = build_diff(data1, data2)

    if format_name == 'stylish':
        return format_stylish(diff)
    elif format_name == 'plain':
        result = format_plain(diff)
        return '\n'.join(result)
    elif format_name == 'json':
        return format_json(diff)
    else:
        raise ValueError(f"Unsupported format: {format_name}")


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        default='stylish',
        help='set format of output (default: stylish)'
    )
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
