# CSV Processor

Утилита для обработки CSV файлов с возможностью фильтрации и агрегирования данных через командную строку.

## Возможности

- Фильтрация данных по условию (например, `price>500`)
- Выполнение агрегатных операций (например, среднее значение по столбцу `rating`)

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/your_username/csv_processor.git
   cd csv_processor
````

2. Создайте и активируйте виртуальное окружение (рекомендуется):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate     # Windows
   ```

3. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

## Использование

```bash
python main.py --file data.csv --filter "price>500"
python main.py --file data.csv --aggregate "rating avg"
```

### Параметры

* `--file` — путь к CSV файлу (обязательно)
* `--filter` — условие фильтрации, например: `price>500`
* `--aggregate` — агрегатная операция, например: `rating avg`

## Структура проекта

```
csv_processor/
├── commands/
│   ├── filter.py
│   └── aggregate.py
├── utils.py
├── main.py
├── requirements.txt
└── README.md
```

## Тестирование

Для запуска тестов используйте:

```bash
pytest
```