import argparse
from gendiff.parser import parse_file


def generate_diff(first_file, second_file):
    data1 = parse_file(first_file)
    data2 = parse_file(second_file)

    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []

    for key in all_keys:
        if key not in data1:
            diff.append(f'  + {key}: {str(data2[key]).lower()}')
        elif key not in data2:
            diff.append(f'  - {key}: {str(data1[key]).lower()}')
        elif data1[key] == data2[key]:
            diff.append(f'    {key}: {str(data1[key]).lower()}')
        else:
            diff.append(f'  - {key}: {str(data1[key]).lower()}')
            diff.append(f'  + {key}: {str(data2[key]).lower()}')

    return '{\n' + '\n'.join(diff) + '\n}'


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
