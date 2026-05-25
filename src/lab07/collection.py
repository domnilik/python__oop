from typing import Optional
from model import BankAccount

class BankOffice:
    
    def __init__(self, office_name: str):
        self.office_name = office_name
        self._items = []

    def add(self, account: BankAccount) -> None:
        if not isinstance(account, BankAccount):
            raise TypeError(f"Можно добавлять только объекты BankAccount, получено: {type(account)}")
        
        if self.find_by_number(account.account_number): 
            raise ValueError(f"Счет с номером {account.account_number} уже существует!")
            
        self._items.append(account)

    def remove(self, account: BankAccount) -> None:
        if account in self._items:
            self._items.remove(account)
        else:
            raise ValueError("Счет не найден в коллекции.")

    def get_all(self):
        return self._items

    def find_by_number(self, number: str) -> Optional[BankAccount]:
        for acc in self._items:
            if acc.account_number == str(number):
                return acc
        return None

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def remove_at(self, index: int) -> BankAccount:
        if 0 <= index < len(self._items):
            return self._items.pop(index)
        raise IndexError("Индекс вне диапазона.")

    def sort_by(self, key_extractor) -> None:
        self._items.sort(key=key_extractor)

    def filter_by(self, predicate) -> 'BankOffice':
        filtered_office = BankOffice(f"Отфильтрованный {self.office_name}")
        filtered_office._items = [item for item in self._items if predicate(item)]
        return filtered_office

    def get_active_accounts(self) -> 'BankOffice':
        return self.filter_by(lambda acc: acc.is_active)

    def __str__(self) -> str:
        return f"Офис '{self.office_name}' (Счетов: {len(self)})"