import csv
from typing import List

def run_aggregate(file_path: str, command: str) -> None:
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        header = reader.fieldnames
        if not header:
            raise ValueError("CSV file does not contain headers.")

        try:
            field, operation = command.split()
        except ValueError:
            raise ValueError(f"Invalid aggregation command format: '{command}'. Expected 'field operation'.")

        if field not in header:
            raise ValueError(f"Column '{field}' not found")

        values: List[float] = []
        for row in reader:
            try:
                values.append(float(row[field]))
            except ValueError:
                raise ValueError(f"Column '{field}' must contain numeric values only")

        if not values:
            raise ValueError(f"No numeric values found in column '{field}' for aggregation.")

        if operation == "avg":
            result: float = sum(values) / len(values)
        elif operation == "min":
            result = min(values)
        elif operation == "max":
            result = max(values)
        else:
            raise ValueError(f"Unsupported function")

        print(f"{operation.upper()} values of '{field}': {result}")
