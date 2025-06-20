from typing import Optional

def compare(val: str, operator: str, target: str) -> bool:
    try:
        a_val = float(val)
        b_val = float(target)
    except ValueError:
        a_val = val
        b_val = target

    if operator == ">":
        return a_val > b_val
    elif operator == "<":
        return a_val < b_val
    elif operator == "=":
        return a_val == b_val
    else:
        raise ValueError(f"Unsupported operator: {operator}")

def parse_filter_condition(condition: str) -> tuple[str, str, str]:
    for op in [">", "<", "="]:
        if op in condition:
            parts = condition.split(op)
            if len(parts) != 2:
                raise ValueError("Invalid filter condition format.")
            column = parts[0].strip()
            value = parts[1].strip()
            return column, op, value
    raise ValueError("Filter condition must contain one of '>', '<', '=' operators.")

def run_filter(file_path: str, condition: str) -> None:
    import csv
    from tabulate import tabulate

    column, operator, target = parse_filter_condition(condition)

    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        if column not in reader.fieldnames:
            raise ValueError(f"Column '{column}' not found in CSV.")

        filtered_rows = [row for row in reader if compare(row[column], operator, target)]

    if not filtered_rows:
        print("No rows match the filter condition.")
        return

    print(tabulate(filtered_rows, headers="keys", tablefmt="grid"))
