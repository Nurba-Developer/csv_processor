import csv
from typing import List

def run_aggregate(file_path: str, command: str) -> None:
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            header = reader.fieldnames
            if not header:
                raise ValueError("CSV file has no header.")

            try:
                field, operation = command.split()
            except ValueError:
                raise ValueError(f"Invalid aggregate command format: '{command}'. Expected 'field operation'.")

            if field not in header:
                raise ValueError(f"Column '{field}' not found in CSV.")

            values: List[float] = []
            for row in reader:
                try:
                    values.append(float(row[field]))
                except ValueError:
                    raise ValueError(f"Column '{field}' must contain numeric values only.")

            if not values:
                raise ValueError(f"No numeric data to aggregate in column '{field}'.")

            if operation == "avg":
                result = sum(values) / len(values)
            elif operation == "min":
                result = min(values)
            elif operation == "max":
                result = max(values)
            else:
                raise ValueError(f"Unsupported function '{operation}'. Supported: avg, min, max.")

            # Форматируем результат в строку с 1 знаком после запятой
            result_str = f"{result:.1f}"

            # Передаем в табулятор строку, чтобы не убрать десятичную часть
            try:
                from tabulate import tabulate
                print(tabulate(
                    [{field: result_str}],  # строка вместо числа
                    headers="keys",
                    tablefmt="grid"
                ))
            except ImportError:
                print(f"{operation.upper()} of '{field}': {result_str}")

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
