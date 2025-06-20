import os

def validate_file_path(file_path: str) -> bool:
    return os.path.isfile(file_path) and file_path.lower().endswith('.csv')
