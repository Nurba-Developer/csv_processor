import csv
from tabulate import tabulate
from csv_processor.models import CsvRow


def parse_filter_condition(condition: str) -> tuple[str, str, str]:
    """Парсит строку фильтра, например price>500 → ('price', '>', '500')"""
    for op in [">=", "<=", ">", "<", "="]:
        if op in condition:
            column, value = condition.split(op)
            return column.strip(), op, value.strip()
    raise ValueError("Unsupported filter operator. Use one of: >, <, =, >=, <=")


def compare(val: str, op: str, target: str) -> bool:
    """Сравнение строковых или числовых значений"""
    try:
        val_num = float(val)
        target_num = float(target)
    except ValueError:
        val_num, target_num = val, target

    if op == ">":
        return val_num > target_num
    elif op == "<":
        return val_num < target_num
    elif op == "=":
        return val_num == target_num
    elif op == ">=":
        return val_num >= target_num
    elif op == "<=":
        return val_num <= target_num
    else:
        raise ValueError("Unknown comparison operator.")


def run_filter(file_path: str, condition: str):
    column, op, value = parse_filter_condition(condition)

    with open(file_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        filtered_rows = []

        for row_data in reader:
            row = CsvRow(row_data)
            if column not in row.data:
                raise ValueError(f"Column '{column}' not found in CSV.")
            if compare(row.get(column), op, value):
                filtered_rows.append(row.data)

    if filtered_rows:
        print(tabulate(filtered_rows, headers="keys", tablefmt="grid"))
    else:
        print("No rows match the filter condition.")
