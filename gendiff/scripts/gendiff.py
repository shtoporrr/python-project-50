import argparse
from gendiff.parser import parse_file
from gendiff.diff_builder import build_diff
from gendiff.formatters.stylish import format_diff


def generate_diff(first_file, second_file, format_name='stylish'):
    """Generate diff between two files."""
    data1 = parse_file(first_file)
    data2 = parse_file(second_file)

    diff = build_diff(data1, data2)

    if format_name == 'stylish':
        return format_diff(diff)
    else:
        raise ValueError(f"Unsupported format: {format_name}")


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
