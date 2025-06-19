from dataclasses import dataclass
from typing import Any


@dataclass
class CsvRow:
    """Объект, представляющий строку CSV"""
    data: dict[str, Any]

    def get(self, key: str) -> Any:
        return self.data.get(key)
