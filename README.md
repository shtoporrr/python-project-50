### Hexlet tests and linter status:
[![Actions Status](https://github.com/shtoporrr/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/shtoporrr/python-project-50/actions)
[![Maintainability](https://codeclimate.com/github/shtoporrr/python-project-50/maintainability)](https://codeclimate.com/github/shtoporrr/python-project-50/maintainability)
[![Test Coverage](https://codeclimate.com/github/shtoporrr/python-project-50/test_coverage)](https://codeclimate.com/github/shtoporrr/python-project-50/test_coverage)
[![Python CI](https://github.com/shtoporrr/python-project-50/actions/workflows/python-ci.yml/badge.svg)](https://github.com/shtoporrr/python-project-50/actions/workflows/python-ci.yml)

# Вычислитель отличий

Утилита для поиска отличий между конфигурационными файлами.

## Установка

```bash
pip install hexlet-code
```

## Использование

### Как библиотека

```python
from gendiff import generate_diff

diff = generate_diff(file_path1, file_path2)
print(diff)
```

### Как CLI-утилита

```bash
gendiff path/to/file1.json path/to/file2.json
```

## Возможности

- Поддержка форматов: JSON
- Генерация отчета в виде plain text
- Поддержка сравнения плоских файлов