# main.py

import argparse
from typing import Optional
from commands.filter import run_filter
from commands.aggregate import run_aggregate

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="CSV Processor: фильтрация и агрегация CSV-файлов"
    )
    parser.add_argument(
        "--file", "-f", required=True, help="Путь к CSV-файлу"
    )
    parser.add_argument(
        "--filter", "-flt", help="Условие фильтрации, например: 'price > 100'"
    )
    parser.add_argument(
        "--aggregate", "-agg", help="Агрегация в формате: 'field operation', например: 'price avg'"
    )
    return parser.parse_args()

def main() -> None:
    args = parse_args()

    if not args.filter and not args.aggregate:
        print("Ошибка: Укажите либо --filter, либо --aggregate")
        return

    try:
        if args.filter:
            run_filter(args.file, args.filter)
        elif args.aggregate:
            run_aggregate(args.file, args.aggregate)
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()