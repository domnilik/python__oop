from base import BankAccount
from validate import validate_amount


class SavingsAccount(BankAccount):
    
    def __init__(self, account_number: str, owner_name: str, balance: float = 0.0, interest_rate: float = 10.0):
<<<<<<< HEAD
=======
        
>>>>>>> 1d053da9af70bec3788e5993c0e011f39bbbd151
        super().__init__(account_number, owner_name, balance)
        self._interest_rate = interest_rate # фунцкия накопления процентов

    def apply_interest(self):
        interest = self._balance * (self._interest_rate / 100)
        self._balance += interest
        self._add_transaction(f"Начисление % (ставка {self._interest_rate}%)", interest)
        return interest

    def __str__(self) -> str:
        return f"[СБЕРЕГАТЕЛЬНЫЙ] {super().__str__()} (Ставка: {self._interest_rate}%)"


class BusinessAccount(BankAccount):
    
    def __init__(self, account_number: str, owner_name: str, balance: float = 0.0, overdraft_limit: float = 1000.0):
        super().__init__(account_number, owner_name, balance)
        self._overdraft_limit = overdraft_limit #позволяет уходить в минус в пределах лимита


    def withdraw(self, amount: float) -> float:
        if not self._is_active:
            raise ValueError("Счет закрыт!")
            
        val = validate_amount(amount)
        available_funds = self._balance + self._overdraft_limit
        
        if val > available_funds:
            raise ValueError(f"Лимит превышен! Доступно (с овердрафтом): {available_funds:.2f}")
        
        self._balance -= val
        self._add_transaction("Снятие (бизнес-овердрафт)", -val)
        return self._balance

    def __str__(self) -> str:
        return f"[БИЗНЕС] {super().__str__()} (Лимит: {self._overdraft_limit} руб.)"


class BankOffice:
    
    def __init__(self, office_name: str):
        self.office_name = office_name
        self._items = []

    def add(self, account: BankAccount):

        if not isinstance(account, BankAccount):
            raise TypeError("Ошибка: можно добавлять только объекты BankAccount и его наследников.")
        self._items.append(account)

    def get_accounts_by_type(self, cls): #метод фильтрации
        return [acc for acc in self._items if isinstance(acc, cls)]

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __str__(self):
        return f"Офис '{self.office_name}' (Всего объектов: {len(self._items)})"
