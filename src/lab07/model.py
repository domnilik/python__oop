from datetime import datetime
from validate import ValidationError, validate_account_number, validate_owner_name, validate_balance, validate_amount

class BankAccount:
    total_accounts = 0  

    def __init__(self, account_number, owner_name, balance=0.0, account_type="Обычный"):
        self._account_number = validate_account_number(account_number)
        self._owner_name = validate_owner_name(owner_name)
        self._balance = validate_balance(balance)
        self._account_type = account_type
        self._is_active = True 
        
        self._transactions = []
        self._add_transaction("Открытие счета", self._balance)
        
        BankAccount.total_accounts += 1

    @property
    def account_number(self):
        return self._account_number

    @property
    def account_type(self):
        return self._account_type

    @property
    def balance(self):
        return self._balance

    @property
    def owner_name(self):
        return self._owner_name

    @owner_name.setter
    def owner_name(self, new_name):
        self._owner_name = validate_owner_name(new_name)
        self._add_transaction("Смена имени владельца", 0)

    @property
    def is_active(self):
        return self._is_active

    def _add_transaction(self, op_type, amount):
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._transactions.append(f"[{date_str}] {op_type}: {amount:.2f} руб.")

    def deposit(self, amount):
        if not self._is_active:
            raise ValidationError("Действие отклонено: Счет закрыт!")
        
        val = validate_amount(amount)
        self._balance += val
        self._add_transaction("Пополнение", val)
        return self._balance

    def withdraw(self, amount):
        if not self._is_active:
            raise ValidationError("Действие отклонено: Счет закрыт!")
        
        val = validate_amount(amount)
        if val > self._balance:
            raise ValidationError(f"Недостаточно средств! Баланс: {self._balance:.2f}")
        
        self._balance -= val
        self._add_transaction("Снятие", -val)
        return self._balance

    def get_history(self):
        if not self._transactions:
            return "История операций пуста."
        return "\n".join(self._transactions)

    def close_account(self):
        if self._balance < 0:
            raise ValidationError(f"Нельзя закрыть счет с задолженностью: {self._balance:.2f}")
        
        self._is_active = False
        self._add_transaction("Счет закрыт", 0)

    def __str__(self):
        return f"{self._account_number:<10} | {self._owner_name:<12} | {self._balance:<10.2f} | {self._account_type}"

    def __repr__(self):
        return f"BankAccount(number='{self._account_number}', owner='{self._owner_name}', type='{self._account_type}')"

    def __eq__(self, other):
        if not isinstance(other, BankAccount):
            return False
        return self._balance == other._balance


class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner_name, balance=0.0, interest_rate=0.1):
        super().__init__(account_number, owner_name, balance, "Сберегательный")
        self.interest_rate = interest_rate

    def apply_interest(self):
        if self._is_active:
            interest = self._balance * self.interest_rate
            self._balance += interest
            self._add_transaction(f"Начисление % ({self.interest_rate * 100:.1f}%)", interest)
            return interest
        return 0


class CheckingAccount(BankAccount):
    def __init__(self, account_number, owner_name, balance=0.0, overdraft_limit=5000.0):
        super().__init__(account_number, owner_name, balance, "Расчетный")
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if not self._is_active:
            raise ValidationError("Действие отклонено: Счет закрыт!")
        
        val = validate_amount(amount)
        if val > (self._balance + self.overdraft_limit):
            available = self._balance + self.overdraft_limit
            raise ValidationError(f"Превышен лимит овердрафта! Доступно: {available:.2f}")
        
        self._balance -= val
        self._add_transaction("Снятие (овердрафт)", -val)
        return self._balance