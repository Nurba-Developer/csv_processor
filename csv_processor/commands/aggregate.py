import csv
from statistics import mean
from csv_processor.models import CsvRow


def run_aggregate(file_path: str, command: str):
    try:
        column, func = command.strip().split()
        func = func.lower()
    except ValueError:
        raise ValueError("Aggregate command must be in format: column function (e.g. rating avg)")
    
    supported_funcs = {"avg", "min", "max"}
    if func not in supported_funcs:
        raise ValueError(f"Unsupported function '{func}'. Use one of: {', '.join(supported_funcs)}")

    values = []

    with open(file_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row_data in reader:
            row = CsvRow(row_data)
            if column not in row.data:
                raise ValueError(f"Column '{column}' not found in CSV.")
            try:
                values.append(float(row.get(column)))
            except ValueError:
                raise ValueError(f"Column '{column}' must contain numeric values only.")

    if not values:
        print("No values to aggregate.")
        return

    if func == "avg":
        result = mean(values)
    elif func == "min":
        result = min(values)
    elif func == "max":
        result = max(values)

    print(f"{func.upper()} of '{column}': {result}")
