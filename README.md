### Hexlet tests and linter status:
[![Actions Status](https://github.com/shtoporrr/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/shtoporrr/python-project-50/actions)

### Description
The `gendiff` utility compares two configuration files and shows the difference. Currently supports JSON format.

### Installation
```bash
pip install hexlet-code
```

### Usage
As CLI utility:
```bash
$ gendiff file1.json file2.json
{
    host: hexlet.io
  - follow: false
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

As library in your code:
```python
from gendiff import generate_diff

diff = generate_diff('file1.json', 'file2.json')
print(diff)
```

### Features
- Compares two JSON files
- Shows differences in a readable format
- Can be used both as CLI tool and library
- Supports different output formats (default: stylish)