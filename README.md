### Hexlet tests and linter status:
[![Actions Status](https://github.com/shtoporrr/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/shtoporrr/python-project-50/actions)
[![Maintainability](https://qlty.sh/badges/e6e05074-620c-46f8-a1da-8e3ea73cb832/maintainability.svg)](https://qlty.sh/gh/shtoporrr/projects/python-project-50)
[![Test Coverage](https://qlty.sh/badges/e6e05074-620c-46f8-a1da-8e3ea73cb832/test_coverage.svg)](https://qlty.sh/gh/shtoporrr/projects/python-project-50)
[![Python CI](https://github.com/shtoporrr/python-project-50/actions/workflows/python-ci.yml/badge.svg)](https://github.com/shtoporrr/python-project-50/actions/workflows/python-ci.yml)

# Difference Generator (Gendiff)

A command-line utility that determines the difference between two configuration files.

## Features

- Supports JSON and YAML formats
- Shows differences in a structured format
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