### Hexlet tests and linter status:
[![Actions Status](https://github.com/shtoporrr/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/shtoporrr/python-project-50/actions)
[![Maintainability](https://qlty.sh/badges/e6e05074-620c-46f8-a1da-8e3ea73cb832/maintainability.svg)](https://qlty.sh/gh/shtoporrr/projects/python-project-50)
[![Test Coverage](https://qlty.sh/badges/e6e05074-620c-46f8-a1da-8e3ea73cb832/test_coverage.svg)](https://qlty.sh/gh/shtoporrr/projects/python-project-50)
[![Python CI](https://github.com/shtoporrr/python-project-50/actions/workflows/python-ci.yml/badge.svg)](https://github.com/shtoporrr/python-project-50/actions/workflows/python-ci.yml)

# Difference Generator (Gendiff)

A command-line utility that determines the difference between two configuration files.

## Features

- **Recursive comparison**: Supports nested JSON and YAML structures
- **Multiple formats**: JSON and YAML file support
- **Multiple output formats**: Stylish (default) and Plain formats
- **Structured output**: Clean, readable diff format with proper indentation
- **Modular architecture**: Separated diff building from formatting for extensibility

## Installation

```bash
make install
```

## Usage

### Command Line

```bash
# Default stylish format
gendiff filepath1.json filepath2.json

# Plain format
gendiff --format plain filepath1.json filepath2.json
```

### Python API

```python
from gendiff import generate_diff

# Default stylish format
diff = generate_diff(file_path1, file_path2)
print(diff)

# Plain format
diff = generate_diff(file_path1, file_path2, 'plain')
print(diff)
```

### Example with nested structures

**file1.json:**
```json
{
  "common": {
    "setting1": "Value 1",
    "setting2": 200,
    "setting3": true,
    "setting6": {
      "key": "value",
      "doge": {
        "wow": ""
      }
    }
  },
  "group1": {
    "baz": "bas",
    "foo": "bar",
    "nest": {
      "key": "value"
    }
  },
  "group2": {
    "abc": 12345,
    "deep": {
      "id": 45
    }
  }
}
```

**file2.json:**
```json
{
  "common": {
    "follow": false,
    "setting1": "Value 1",
    "setting3": null,
    "setting4": "blah blah",
    "setting5": {
      "key5": "value5"
    },
    "setting6": {
      "key": "value",
      "ops": "vops",
      "doge": {
        "wow": "so much"
      }
    }
  },
  "group1": {
    "foo": "bar",
    "baz": "bars",
    "nest": "str"
  },
  "group3": {
    "deep": {
      "id": {
        "number": 45
      }
    },
    "fee": 100500
  }
}
```

**Stylish format output:**
```
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

**Plain format output:**
```
Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]
```