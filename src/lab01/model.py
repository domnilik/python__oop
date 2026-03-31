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
        self._add_transaction("Открытие счета", self._balance)
        
        BankAccount.total_accounts += 1

    @property
    def balance(self):
        """Свойство для чтения баланса (инкапсуляция)"""
        return self._balance

    @property
    def owner_name(self):
        return self._owner_name

    @owner_name.setter
    def owner_name(self, new_name):
        """Сеттер с валидацией для безопасного изменения имени"""
        self._owner_name = validate_owner_name(new_name)
        self._add_transaction("Смена имени владельца", 0)

    @property
    def is_active(self):
        return self._is_active

    def _add_transaction(self, op_type, amount):
        """Внутренний приватный метод для логирования операций"""
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._transactions.append(f"[{date_str}] {op_type}: {amount:.2f} руб.")

    def deposit(self, amount):
        """Метод пополнения счета"""
        if not self._is_active:
            raise ValueError("Действие отклонено: Счет закрыт!")
        
        val = validate_amount(amount)
        self._balance += val
        self._add_transaction("Пополнение", val)
        return self._balance

    def withdraw(self, amount):
        """Метод снятия средств с учетом кредитного лимита"""
        if not self._is_active:
            raise ValueError("Действие отклонено: Счет закрыт!")
        
        val = validate_amount(amount)
      
        if val > (self._balance + self._credit_limit):
            available = self._balance + self._credit_limit
            raise ValueError(f"Недостаточно средств! Доступно (с учетом лимита): {available:.2f}")
        
        self._balance -= val
        self._add_transaction("Снятие", -val)
        return self._balance

    def apply_interest(self):
        """Начисление процентов (только для сберегательных счетов)"""
        if self._account_type == "Сберегательный" and self._is_active:
            interest = self._balance * (self._interest_rate / 100)
            self._balance += interest
            self._add_transaction(f"Начисление % ({self._interest_rate}%)", interest)
            return interest
        return 0

    def get_history(self):
        """Возвращает форматированную историю операций"""
        if not self._transactions:
            return "История операций пуста."
        return "\n".join(self._transactions)

    def close_account(self):
        """Закрытие счета (изменение состояния объекта)"""
        if self._balance < 0:
            raise ValueError(f"Нельзя закрыть счет с задолженностью: {self._balance:.2f}")
        
        self._is_active = False
        self._add_transaction("Счет закрыт", 0)

    def __str__(self):
        status = "Активен" if self._is_active else "Закрыт"
        return f"[{self._account_type}] {self._owner_name} | Баланс: {self._balance:.2f} руб. | Статус: {status}"

    def __repr__(self):
        return f"BankAccount(number='{self._account_number}', owner='{self._owner_name}', type='{self._account_type}')"

    def __eq__(self, other):
        """Сравнение счетов по их финансовому весу (балансу)"""
        if not isinstance(other, BankAccount):
            return False
        return self._balance == other._balance