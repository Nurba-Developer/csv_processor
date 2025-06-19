import os


def validate_file_path(path: str) -> bool:
    """Проверка, существует ли CSV-файл и имеет ли правильное расширение"""
    return os.path.isfile(path) and path.lower().endswith(".csv")
