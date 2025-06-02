### Hexlet tests and linter status:
[![Actions Status](https://github.com/shtoporrr/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/shtoporrr/python-project-50/actions)
[![Maintainability](https://qlty.sh/badges/e6e05074-620c-46f8-a1da-8e3ea73cb832/maintainability.svg)](https://qlty.sh/gh/shtoporrr/projects/python-project-50)
[![Test Coverage](https://qlty.sh/badges/e6e05074-620c-46f8-a1da-8e3ea73cb832/test_coverage.svg)](https://qlty.sh/gh/shtoporrr/projects/python-project-50)
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