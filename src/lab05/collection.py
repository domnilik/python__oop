from model import BankAccount

class BankOffice:
    def __init__(self, office_name, accounts=None):
        self.office_name = office_name
        self._items = accounts if accounts is not None else []

    def add(self, account):
        if isinstance(account, BankAccount):
            self._items.append(account)
        return self

    def sort_by(self, key_func, reverse=False):
        self._items.sort(key=key_func, reverse=reverse)
        return self

    def filter_by(self, predicate):
        filtered_list = list(filter(predicate, self._items))
        return BankOffice(f"Filtered {self.office_name}", filtered_list)

    def apply(self, func):
        for item in self._items:
            func(item)
        return self

    def get_summaries(self):
        return list(map(lambda acc: f"{acc.owner_name}: {acc.balance:.2f}", self._items))

    def __str__(self):
        status = f"--- {self.office_name} (Счетов: {len(self._items)}) ---\n"
        content = "\n".join([str(item) for item in self._items])
        return status + (content if content else "Пусто")