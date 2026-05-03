from datetime import datetime
from validate import *

class BankAccount:
    total_accounts = 0  

    def __init__(self, account_number: str, owner_name: str, balance: float = 0.0):
        self._account_number = validate_account_number(account_number)
        self._owner_name = validate_owner_name(owner_name)
        self._balance = validate_balance(balance)
        self._is_active = True 
        self._transactions = []
        
        self._add_transaction("Открытие счета", self._balance)
        BankAccount.total_accounts += 1

  
    @property
    def balance(self) -> float: return self._balance

    @property
    def owner_name(self) -> str: return self._owner_name

    @property
    def is_active(self) -> bool: return self._is_active

    def _add_transaction(self, op_type: str, amount: float):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._transactions.append(f"[{date}] {op_type}: {amount:.2f} руб.")

    def _check_active(self): #метод, чтобы не дублировать if в deposit и withdraw
        if not self._is_active:
            raise ValueError("Действие отклонено: Счет закрыт!")

    def deposit(self, amount: float) -> float:
        self._check_active()
        val = validate_amount(amount)
        self._balance += val
        self._add_transaction("Пополнение", val)
        return self._balance

    def withdraw(self, amount: float) -> float:
        self._check_active()
        val = validate_amount(amount)
        if val > self._balance:
            raise ValueError(f"Недостаточно средств! Баланс: {self._balance:.2f}")
        
        self._balance -= val
        self._add_transaction("Снятие", -val)
        return self._balance

    def get_history(self) -> str:
        return "\n".join(self._transactions) if self._transactions else "История пуста."

    def __str__(self) -> str:
        status = "Активен" if self._is_active else "Закрыт"
        return f"{self._owner_name} | Баланс: {self._balance:.2f} | {status}"
