from lab01.validation import *

class BankAccount:
    bank_name = "Python Bank"
    total_accounts = 0
    
    def __init__(self, account_number, owner_name, initial_balance=0, credit_limit=0, interest_rate=0):
        validate_account_number(account_number)
        validate_owner_name(owner_name)
        validate_balance(initial_balance)
        validate_credit_limit(credit_limit)
        validate_interest_rate(interest_rate)
        
        self.__account_number = account_number.strip()
        self.__owner_name = owner_name.strip()
        self.__balance = float(initial_balance)
        self.__credit_limit = float(credit_limit)
        self.__interest_rate = float(interest_rate)
        self.__is_active = True
        self.__transactions = []
        
        BankAccount.total_accounts += 1
        self.__add_transaction("CREATION", 0, f"Счет создан. Баланс: {self.__balance}")
    
    @property
    def account_number(self):
        return self.__account_number
    
    @property
    def owner_name(self):
        return self.__owner_name
    
    @property
    def balance(self):
        return self.__balance
    
    @property
    def credit_limit(self):
        return self.__credit_limit
    
    @credit_limit.setter
    def credit_limit(self, value):
        if not self.__is_active:
            raise ValueError("Нельзя изменить кредитный лимит закрытого счета")
        validate_credit_limit(value)
        old_limit = self.__credit_limit
        self.__credit_limit = float(value)
        self.__add_transaction("LIMIT_CHANGE", 0, f"Кредитный лимит изменен: {old_limit} -> {self.__credit_limit}")
    
    @property
    def interest_rate(self):
        return self.__interest_rate
    
    @interest_rate.setter
    def interest_rate(self, value):
        if not self.__is_active:
            raise ValueError("Нельзя изменить процентную ставку закрытого счета")
        validate_interest_rate(value)
        old_rate = self.__interest_rate
        self.__interest_rate = float(value)
        self.__add_transaction("RATE_CHANGE", 0, f"Процентная ставка изменена: {old_rate}% -> {self.__interest_rate}%")
    
    @property
    def is_active(self):
        return self.__is_active
    
    @property
    def transactions(self):
        return self.__transactions.copy()
    
    @property
    def available_funds(self):
        return self.__balance + self.__credit_limit
    
    def __add_transaction(self, transaction_type, amount, description):
        from datetime import datetime
        transaction = {
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'type': transaction_type,
            'amount': amount,
            'balance_after': self.__balance,
            'description': description
        }
        self.__transactions.append(transaction)
    
    def deposit(self, amount):
        if not self.__is_active:
            raise ValueError("Нельзя пополнить закрытый счет")
        if not isinstance(amount, (int, float)):
            raise TypeError(f"Сумма должна быть числом, получена {type(amount).__name__}")
        if amount <= 0:
            raise ValueError(f"Сумма пополнения должна быть положительной: {amount}")
        
        self.__balance += amount
        self.__add_transaction("DEPOSIT", amount, f"Пополнение на {amount:.2f}")
        return self.__balance
    
    def withdraw(self, amount):
        if not self.__is_active:
            raise ValueError("Нельзя снять средства с закрытого счета")
        validate_withdrawal(self.__balance, amount, self.__credit_limit)
        
        self.__balance -= amount
        self.__add_transaction("WITHDRAWAL", -amount, f"Снятие {amount:.2f}")
        return self.__balance
    
    def close_account(self):
        if not self.__is_active:
            raise ValueError("Счет уже закрыт")
        if self.__balance > 0:
            raise ValueError(f"Невозможно закрыть счет с положительным балансом. Текущий баланс: {self.__balance:.2f}")
        if self.__balance < 0:
            raise ValueError(f"Невозможно закрыть счет с отрицательным балансом. Текущий баланс: {self.__balance:.2f}")
        
        self.__is_active = False
        self.__add_transaction("CLOSE", 0, "Счет закрыт")
        return True
    
    def activate_account(self):
        if self.__is_active:
            raise ValueError("Счет уже активен")
        
        self.__is_active = True
        self.__add_transaction("ACTIVATE", 0, "Счет активирован")
        return True
    
    def apply_interest(self):
        if not self.__is_active:
            raise ValueError("Нельзя начислить проценты на закрытый счет")
        
        if self.__balance <= 0:
            interest = 0
        else:
            interest = self.__balance * (self.__interest_rate / 100)
            self.__balance += interest
        
        self.__add_transaction("INTEREST", interest, f"Начислены проценты по ставке {self.__interest_rate}%: {interest:.2f}")
        return interest
    
    def __str__(self):
        status = "АКТИВЕН" if self.__is_active else "ЗАКРЫТ"
        return (f"Счет {self.__account_number}\n"
                f"Владелец: {self.__owner_name}\n"
                f"Баланс: {self.__balance:,.2f} руб.\n"
                f"Кредитный лимит: {self.__credit_limit:,.2f} руб.\n"
                f"Доступно: {self.available_funds:,.2f} руб.\n"
                f"Ставка: {self.__interest_rate}%\n"
                f"Статус: {status}")
    
    def __repr__(self):
        return (f"BankAccount('{self.__account_number}', '{self.__owner_name}', "
                f"balance={self.__balance:.2f}, credit_limit={self.__credit_limit:.2f}, "
                f"interest_rate={self.__interest_rate:.2f}, active={self.__is_active})")
    
    def __eq__(self, other):
        if not isinstance(other, BankAccount):
            return False
        return self.__account_number == other.__account_number
    
    def __lt__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented
        return self.__balance < other.__balance 