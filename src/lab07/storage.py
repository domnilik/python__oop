import json
import os
from typing import List, Dict, Any

def save(accounts_data: List[Dict[str, Any]], filepath: str) -> None:
    """Сохранить коллекцию в JSON-файл."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(accounts_data, f, ensure_ascii=False, indent=4)

def load(filepath: str) -> List[Dict[str, Any]]:
    """Загрузить объекты из JSON-файла."""
    if not os.path.exists(filepath):
        return []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []