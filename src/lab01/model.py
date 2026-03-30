from datetime import datetime
from validate import *

class BankAccount:
    total_accounts = 0 

    def __init__(self, account_number, owner_name, balance=0.0, account_type="Обычный"):
        self._account_number = validate_account_number(account_number)
        self._owner_name = validate_owner_name(owner_name)
        self._balance = validate_balance(balance)
        self._account_type = account_type
        
        self._credit_limit = 1000.0 if account_type == "Бизнес" else 0.0
        self._interest_rate = 10.0 if account_type == "Сберегательный" else 0.0
        self._is_active = True 
        self._transactions = []
        
        BankAccount.total_accounts += 1

    @property
    def balance(self):
        return self._balance

    @property
    def owner_name(self):
        return self._owner_name

    @owner_name.setter
    def owner_name(self, new_name):
        self._owner_name = validate_owner_name(new_name)

    def __str__(self):
        return f"[{self._account_type}] {self._owner_name} | Баланс: {self._balance:.2f} руб."

    def __repr__(self):
        return f"BankAccount(number='{self._account_number}', owner='{self._owner_name}')"

    def __eq__(self, other):
        if not isinstance(other, BankAccount):
            return False
        return self._balance == other._balance

    def deposit(self, amount):
        if not self._is_active:
            raise ValueError("Действие отклонено: Счет закрыт!")
        val = validate_amount(amount)
        self._balance += val
        return self._balance

    def withdraw(self, amount):
        if not self._is_active:
            raise ValueError("Действие отклонено: Счет закрыт!")
        val = validate_amount(amount)
        if val > (self._balance + self._credit_limit):
            raise ValueError(f"Недостаточно средств! Лимит овердрафта: {self._credit_limit}")
        self._balance -= val
        return self._balance

    def close_account(self):
        self._is_active = False