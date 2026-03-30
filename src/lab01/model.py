from datetime import datetime
from validate import *

class BankAccount:
    total_accounts = 0

    def __init__(self, account_number, owner_name, balance=0.0, credit_limit=0.0):
        self._account_number = validate_account_number(account_number)
        self._owner_name = validate_owner_name(owner_name)
        self._balance = validate_balance(balance)
        self._credit_limit = validate_credit_limit(credit_limit)
        
        self._is_active = True
        self._transactions = []
        BankAccount.total_accounts += 1
        self._add_transaction("CREATION", 0, "Счет успешно открыт")

    @property
    def balance(self): return self._balance
    
    @property
    def owner_name(self): return self._owner_name

    @property
    def transactions(self): return self._transactions.copy()

    @property
    def available_funds(self): return self._balance + self._credit_limit

    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts

    def _add_transaction(self, t_type, amount, desc):
        self._transactions.append({
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'type': t_type, 
            'amount': amount, 
            'description': desc
        })

    def deposit(self, amount):
        if not self._is_active: raise ValueError("Счет закрыт")
        if amount <= 0: raise ValueError("Сумма пополнения должна быть положительной")
        self._balance += amount
        self._add_transaction("DEPOSIT", amount, f"Пополнение баланса")
        return self._balance

    def withdraw(self, amount):
        if not self._is_active: raise ValueError("Счет закрыт")
        if amount <= 0: raise ValueError("Сумма снятия должна быть положительной")
        if amount > self.available_funds:
            raise ValueError(f"Недостаточно средств (доступно с лимитом: {self.available_funds})")
        self._balance -= amount
        self._add_transaction("WITHDRAW", -amount, f"Снятие средств")
        return self._balance

    def calculate_annual_bonus(self):
        return self._balance * 0.01

    def __str__(self):
        return f"[{self.__class__.__name__}] {self._owner_name} | Баланс: {self._balance:.2f}"


class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner_name, balance, interest_rate=5.0):
        super().__init__(account_number, owner_name, balance, credit_limit=0.0)
        self._interest_rate = validate_interest_rate(interest_rate)

    def apply_interest(self):
        interest = self._balance * (self._interest_rate / 100)
        self.deposit(interest)
        return interest

    def calculate_annual_bonus(self):
        return self._balance * (self._interest_rate / 100)


class BusinessAccount(BankAccount):
    def __init__(self, account_number, owner_name, balance, tax_id="000"):
        super().__init__(account_number, owner_name, balance, credit_limit=1000.0)
        self._tax_id = tax_id
        self._service_fee = 50.0

    def pay_service_fee(self):
        return self.withdraw(self._service_fee)

    def calculate_annual_bonus(self):
        return 0.0