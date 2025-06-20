
# CSV Processor

Консольное Python-приложение для обработки CSV-файлов с функциями фильтрации и агрегации.

## Возможности

- Фильтрация строк по условию: `filter <column> <operation> <value>`
- Агрегация данных по числовым колонкам: `aggregate <column> <operation>`
- Поддерживаемые операции: `avg`, `min`, `max`

## Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/<your-username>/csv_processor.git
cd csv_processor
````

2. Установите зависимости:

```bash
pip install -r requirements.txt
```

*Или через `pyproject.toml` (если используется Poetry или PEP 621):*

```bash
pip install .
```

## Использование

```bash
python main.py filter <filename.csv> <column> <operation> <value>
```

Пример:

```bash
python main.py filter sample.csv price > 100
```

```bash
python main.py aggregate <filename.csv> <column> <operation>
```

Пример:

```bash
python main.py aggregate data.csv price avg
```

## Поддерживаемые операторы

### Для `filter`:

* `==` — равно
* `!=` — не равно
* `>` — больше
* `<` — меньше
* `>=` — больше или равно
* `<=` — меньше или равно

### Для `aggregate`:

* `avg` — среднее значение
* `min` — минимальное значение
* `max` — максимальное значение

## Тестирование

```bash
pytest
```

Покрытие тестами:

* Проверка фильтрации по числовым и строковым полям
* Проверка агрегации по числовым значениям
* Обработка ошибок: отсутствующая колонка, некорректная команда, нечисловые значения

## Структура проекта

```
csv_processor/
├── commands/
│   ├── __init__.py
│   ├── filter.py
│   └── aggregate.py
├── tests/
│   ├── test_filter.py
│   └── test_aggregate.py
├── main.py
├── requirements.txt
└── README.md
```

## Требования

* Python 3.10+
* `pytest` для запуска тестов