### Hexlet tests and linter status:
[![Actions Status](https://github.com/shtoporrr/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/shtoporrr/python-project-50/actions)
[![Maintainability](https://qlty.sh/badges/e6e05074-620c-46f8-a1da-8e3ea73cb832/maintainability.svg)](https://qlty.sh/gh/shtoporrr/projects/python-project-50)
[![Test Coverage](https://qlty.sh/badges/e6e05074-620c-46f8-a1da-8e3ea73cb832/test_coverage.svg)](https://qlty.sh/gh/shtoporrr/projects/python-project-50)
[![Python CI](https://github.com/shtoporrr/python-project-50/actions/workflows/python-ci.yml/badge.svg)](https://github.com/shtoporrr/python-project-50/actions/workflows/python-ci.yml)

# Difference Generator (Gendiff)

A command-line utility that determines the difference between two configuration files.

## Features

- Supports JSON and YAML formats
- Recursive comparison of nested structures
- Shows differences in a structured stylish format
- Modular architecture with separate diff building and formatting
- Simple and easy to use

## Installation

```bash
make install
```

## Usage

```bash
gendiff file1.json file2.json
gendiff file1.yml file2.yml
```

### Example

#### Simple files:
```
$ gendiff file1.json file2.json
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

#### Nested structures:
```
$ gendiff nested_file1.json nested_file2.json
{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}
```