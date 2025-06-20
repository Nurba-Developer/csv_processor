# csv_processor/commands/filter.py

import csv
from typing import Tuple

def parse_filter_condition(condition: str) -> Tuple[str, str, str]:
    """
    Парсит строку условия фильтрации, например "price>100"
    Возвращает кортеж: (поле, оператор, значение)
    Поддерживаются операторы: =, !=, >, <, >=, <=
    """
    operators = ['>=', '<=', '!=', '=', '>', '<']
    for op in operators:
        if op in condition:
            parts = condition.split(op)
            if len(parts) == 2:
                field = parts[0].strip()
                value = parts[1].strip()
                # Внутри кода будем использовать '=' вместо '=='
                if op == '=':
                    op = '='
                return field, op, value
    raise ValueError(f"Некорректный формат условия фильтрации: '{condition}'")

def compare(val: str, op: str, target: str) -> bool:
    """
    Сравнивает val и target согласно оператору op.
    Попытка сравнения чисел, если возможно.
    """
    try:
        val_num = float(val)
        target_num = float(target)
        if op == '=':
            return val_num == target_num
        elif op == '!=':
            return val_num != target_num
        elif op == '>':
            return val_num > target_num
        elif op == '<':
            return val_num < target_num
        elif op == '>=':
            return val_num >= target_num
        elif op == '<=':
            return val_num <= target_num
        else:
            raise ValueError(f"Неподдерживаемый оператор: {op}")
    except ValueError:
        # Если не числа, сравниваем как строки
        if op == '=':
            return val == target
        elif op == '!=':
            return val != target
        else:
            raise ValueError(f"Оператор '{op}' не поддерживается для строковых значений")

def run_filter(file_path: str, condition: str) -> None:
    """
    Фильтрует CSV-файл по условию и выводит результат таблицей.
    """
    field, op, value = parse_filter_condition(condition)

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        header = reader.fieldnames
        if not header:
            raise ValueError("CSV-файл не содержит заголовков.")
        if field not in header:
            raise ValueError(f"Колонки '{field}' нет в CSV.")

        filtered_rows = []
        for row in reader:
            if compare(row[field], op, value):
                filtered_rows.append(row)

    from tabulate import tabulate
    if filtered_rows:
        print(tabulate(filtered_rows, headers="keys", tablefmt="grid"))
    else:
        print("Нет подходящих записей для заданного условия фильтрации.")
