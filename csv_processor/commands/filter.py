# commands/filter.py

import csv
from typing import List, Callable

def run_filter(file_path: str, filter_command: str) -> None:
    operators = {
        '>': lambda a, b: a > b,
        '<': lambda a, b: a < b,
        '=': lambda a, b: a == b,
        '==': lambda a, b: a == b,
    }

    try:
        field, op, value = filter_command.split(maxsplit=2)
    except ValueError:
        raise ValueError("Неверный формат команды фильтрации. Ожидается 'field operator value'")

    if op not in operators:
        raise ValueError(f"Неподдерживаемый оператор фильтрации: '{op}'. Поддерживаются: {', '.join(operators.keys())}")

    comp_func = operators[op]

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        header = reader.fieldnames
        if not header:
            raise ValueError("CSV-файл не содержит заголовков.")
        if field not in header:
            raise ValueError(f"Колонки '{field}' нет в CSV.")

        filtered_rows = []

        for row in reader:
            cell = row[field]
            # Пытаемся привести к числу, если можно, иначе сравниваем как строки
            try:
                cell_val = float(cell)
                value_val = float(value)
            except ValueError:
                cell_val = cell
                value_val = value
            if comp_func(cell_val, value_val):
                filtered_rows.append(row)

        if not filtered_rows:
            print("Нет строк, соответствующих условию фильтрации.")
            return

        # Красивый вывод с помощью tabulate, если есть
        try:
            from tabulate import tabulate
            print(tabulate(filtered_rows, headers="keys", tablefmt="grid"))
        except ImportError:
            # Вывод простым текстом, если tabulate не установлен
            for row in filtered_rows:
                print(row)