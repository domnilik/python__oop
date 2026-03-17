## Лаба 1

#### model 
```python
from validate import *

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
    
    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts
    
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
```


#### validate

```python
def validate_balance(value):
    if not isinstance(value, (int, float)):
        raise TypeError(f"Баланс должен быть числом, получен {type(value).__name__}")
    if value < 0:
        raise ValueError(f"Баланс не может быть отрицательным: {value}")
    return True

def validate_credit_limit(value):
    if not isinstance(value, (int, float)):
        raise TypeError(f"Кредитный лимит должен быть числом, получен {type(value).__name__}")
    if value < 0:
        raise ValueError(f"Кредитный лимит не может быть отрицательным: {value}")
    return True

def validate_interest_rate(value):
    if not isinstance(value, (int, float)):
        raise TypeError(f"Процентная ставка должна быть числом, получен {type(value).__name__}")
    if value < 0 or value > 100:
        raise ValueError(f"Процентная ставка должна быть от 0 до 100, получена {value}")
    return True

def validate_account_number(value):
    if not isinstance(value, str):
        raise TypeError(f"Номер счета должен быть строкой, получен {type(value).__name__}")
    if not value.strip():
        raise ValueError("Номер счета не может быть пустым")
    if len(value.strip()) < 5:
        raise ValueError(f"Номер счета должен содержать минимум 5 символов, получено {len(value)}")
    return True

def validate_owner_name(value):
    if not isinstance(value, str):
        raise TypeError(f"Имя владельца должно быть строкой, получен {type(value).__name__}")
    if not value.strip():
        raise ValueError("Имя владельца не может быть пустым")
    if len(value.strip()) < 2:
        raise ValueError(f"Имя владельца должно содержать минимум 2 символа, получено {len(value)}")
    return True

def validate_withdrawal(balance, amount, credit_limit=0):
    if not isinstance(amount, (int, float)):
        raise TypeError(f"Сумма должна быть числом, получена {type(amount).__name__}")
    if amount <= 0:
        raise ValueError(f"Сумма для снятия должна быть положительной: {amount}")
    available_funds = balance + credit_limit
    if amount > available_funds:
        raise ValueError(f"Недостаточно средств. Доступно: {available_funds:.2f}, запрошено: {amount:.2f}")
    return True
```


#### demo
```python
from model import BankAccount

def demo_basic_operations():
    print("=" * 50)
    print("ДЕМОНСТРАЦИЯ БАЗОВЫХ ОПЕРАЦИЙ")
    print("=" * 50)
    account = BankAccount("AC001", "Иван Петров", 1000, 500, 5.5)
    print(account)
    print(f"\nВсего счетов создано: {BankAccount.get_total_accounts()}")
    print(f"Представление объекта: {repr(account)}")
    print()

def demo_properties_and_setters():
    print("=" * 50)
    print("СВОЙСТВА И СЕТТЕРЫ")
    print("=" * 50)
    account = BankAccount("AC002", "Мария Сидорова", 2000, 1000, 3.5)
    print(f"Текущий кредитный лимит: {account.credit_limit}")
    account.credit_limit = 2000
    print(f"Новый кредитный лимит: {account.credit_limit}")
    
    print("\nПопытка установить отрицательный кредитный лимит:")
    try:
        account.credit_limit = -500
    except ValueError as e:
        print(f"Ошибка: {e}")
    print()

def demo_business_methods():
    print("=" * 50)
    print("БИЗНЕС-МЕТОДЫ")
    print("=" * 50)
    account = BankAccount("AC003", "Алексей Смирнов", 5000, 2000, 6.0)
    print(f"Начальный баланс: {account.balance}")
    
    # Пополнение счета
    account.deposit(1500)
    print(f"После пополнения на 1500: {account.balance}")
    
    # Снятие со счета
    account.withdraw(2000)
    print(f"После снятия 2000: {account.balance}")
    
    # Начисление процентов
    interest = account.apply_interest()
    print(f"Начислены проценты: {interest:.2f}")
    print(f"Баланс после процентов: {account.balance}")
    
    # Информация о доступных средствах
    print(f"Доступные средства (с учетом кредитного лимита): {account.available_funds}")
    print()

def demo_transaction_history():
    print("=" * 50)
    print("ИСТОРИЯ ТРАНЗАКЦИЙ")
    print("=" * 50)
    account = BankAccount("AC004", "Елена Николаева", 3000, 1000, 4.0)
    
    # Проведем несколько операций
    account.deposit(500)
    account.withdraw(200)
    account.credit_limit = 1500
    account.apply_interest()
    
    print("История операций по счету:")
    for i, trans in enumerate(account.transactions, 1):
        print(f"{i}. {trans['date']} | {trans['type']:10} | {trans['amount']:10.2f} | {trans['description']}")
    print()

def demo_account_comparison():
    print("=" * 50)
    print("СРАВНЕНИЕ СЧЕТОВ")
    print("=" * 50)
    acc1 = BankAccount("AC005", "Петр Сидоров", 5000, 2000, 5.0)
    acc2 = BankAccount("AC006", "Анна Иванова", 3000, 2000, 5.0)
    acc3 = BankAccount("AC005", "Дубликат", 1000, 1000, 3.0)  # Тот же номер
    
    print(f"acc1 == acc2: {acc1 == acc2} (разные счета)")
    print(f"acc1 == acc3: {acc1 == acc3} (одинаковый номер счета)")
    print(f"acc1 < acc2: {acc1 < acc2} (сравнение по балансу)")
    print(f"acc2 < acc1: {acc2 < acc1} (сравнение по балансу)")
    print()

def demo_account_closure():
    print("=" * 50)
    print("ЗАКРЫТИЕ СЧЕТА")
    print("=" * 50)
    account = BankAccount("AC007", "Дмитрий Петров", 0, 0, 3.0)
    print(account)
    
    print("\nЗакрытие счета с нулевым балансом:")
    account.close_account()
    print(f"Статус счета после закрытия: {'Активен' if account.is_active else 'Закрыт'}")
    
    print("\nПопытка операции с закрытым счетом:")
    try:
        account.deposit(1000)
    except ValueError as e:
        print(f"Ошибка: {e}")
    print()

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ КЛАССА BankAccount")
    print("=" * 60 + "\n")
    
    demo_basic_operations()
    demo_properties_and_setters()
    demo_business_methods()
    demo_transaction_history()
    demo_account_comparison()
    demo_account_closure()
    
    print("=" * 60)
    print(f"Всего создано счетов: {BankAccount.get_total_accounts()}")
    print("=" * 60)
```

![](src/images/image1.png)

![](/src/images/image2.png)