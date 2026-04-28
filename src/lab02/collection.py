from model import BankAccount

class BankOffice:
    def __init__(self, office_name):
        self.office_name = office_name
        self._items = []

    def add(self, account):
        if not isinstance(account, BankAccount):
            raise TypeError(f"Можно добавлять только объекты BankAccount, получено: {type(account)}")
        
        if self.find_by_number(account._account_number): #защита от дубликатов
            raise ValueError(f"Счет с номером {account._account_number} уже существует!")
            
        self._items.append(account)

    def remove(self, account):
        if account in self._items:
            self._items.remove(account)
        else:
            raise ValueError("Счет не найден в коллекции.")

    def get_all(self):
        return self._items

    def find_by_number(self, number):
        for acc in self._items:
            if acc._account_number == str(number):
                return acc
        return None

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def remove_at(self, index):
        if 0 <= index < len(self._items):
            return self._items.pop(index)
        raise IndexError("Индекс вне диапазона.")

    def sort_by_balance(self, reverse=False):
        self._items.sort(key=lambda acc: acc.balance, reverse=reverse)

    def get_active_accounts(self):
        new_office = BankOffice(f"Active accounts of {self.office_name}")
        for acc in self._items:
            if acc.is_active:
                new_office.add(acc)
        return new_office

    def __str__(self):
        return f"Офис '{self.office_name}' (Счетов: {len(self)})"