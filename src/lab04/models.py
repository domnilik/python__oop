from datetime import datetime
from interfaces import Printable, Comparable

class BankAccount:
    total_accounts = 0  

    def __init__(self, account_number, owner_name, balance=0.0, account_type="Обычный"):
        # Присваиваем напрямую без лишних функций-валидаторов
        self._account_number = account_number
        self._owner_name = owner_name
        self._balance = balance
        self._account_type = account_type
        self._is_active = True 
        self._transactions = []
        
        # Оставляем только базовую логику
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._transactions.append(f"[{date_str}] Открытие счета: {self._balance:.2f}")
        BankAccount.total_accounts += 1

    @property
    def balance(self): return self._balance

    @property
    def account_number(self): return self._account_number

    @property
    def owner_name(self): return self._owner_name

    def __str__(self):
        return f"[{self._account_type}] {self._owner_name} | Баланс: {self._balance:.2f}"

# --- Классы наследники (ЛР-4) ---

class SavingsAccount(BankAccount, Printable, Comparable):
    def __init__(self, number, owner, balance, interest_rate):
        super().__init__(number, owner, balance, account_type="Сберегательный")
        self.__interest_rate = interest_rate

    def to_string(self) -> str:
        return f"[Savings] №{self.account_number} | Владелец: {self.owner_name} | Ставка: {self.__interest_rate}%"

    def compare_to(self, other) -> float:
        # Просто сравниваем балансы
        return self.balance - other.balance

class BusinessAccount(BankAccount, Printable, Comparable):
    def __init__(self, number, owner, balance, overdraft_limit):
        super().__init__(number, owner, balance, account_type="Бизнес")
        self.__overdraft_limit = overdraft_limit

    def to_string(self) -> str:
        return f"[Business] №{self.account_number} | Владелец: {self.owner_name} | Лимит: {self.__overdraft_limit}"

    def compare_to(self, other) -> float:
        return self.balance - other.balance