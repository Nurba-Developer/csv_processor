# Стартовая точка main.py
import argparse
import sys
from csv_processor.commands.filter import run_filter
from csv_processor.commands.aggregate import run_aggregate
from csv_processor.utils import validate_file_path


def main():
    parser = argparse.ArgumentParser(description="CSV Processor")
    parser.add_argument("--file", type=str, required=True, help="Path to CSV file")
    parser.add_argument("--filter", type=str, help="Filter condition, e.g. price>500")
    parser.add_argument("--aggregate", type=str, help="Aggregate command, e.g. rating avg")

    args = parser.parse_args()

    if not validate_file_path(args.file):
        print("Invalid file path or file not found.")
        sys.exit(1)

    try:
        if args.filter:
            run_filter(args.file, args.filter)
        elif args.aggregate:
            run_aggregate(args.file, args.aggregate)
        else:
            print("Please provide --filter or --aggregate option.")
            parser.print_help()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
