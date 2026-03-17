from lab01.model import BankAccount
from lab01.validation import *

def print_separator(title):
    print("\n" + "="*60)
    print(f" {title}")
    print("="*60)

def demo_basic_operations():
    print_separator("1. БАЗОВЫЕ ОПЕРАЦИИ")
    account = BankAccount("ACC001", "Иван Петров", 1000, 500, 5.5)
    print(account)
    print(f"\nБанк: {BankAccount.bank_name}")
    print(f"Всего счетов: {BankAccount.total_accounts}")
    print(repr(account))

def demo_properties_and_setters():
    print_separator("2. СВОЙСТВА И СЕТТЕРЫ")
    account = BankAccount("ACC002", "Мария Сидорова", 2000, 1000, 3.5)
    print(f"Кредитный лимит: {account.credit_limit}")
    account.credit_limit = 2000
    print(f"Новый кредитный лимит: {account.credit_limit}")
    try:
        account.credit_limit = -500
    except ValueError as e:
        print(f"Ошибка: {e}")

def demo_business_methods():
    print_separator("3. БИЗНЕС-МЕТОДЫ")
    account = BankAccount("ACC003", "Алексей Смирнов", 5000, 2000, 6.0)
    print(f"Баланс: {account.balance}")
    account.deposit(1500)
    print(f"После пополнения: {account.balance}")
    account.withdraw(2000)
    print(f"После снятия: {account.balance}")
    try:
        account.withdraw(10000)
    except ValueError as e:
        print(f"Ошибка: {e}")
    account.apply_interest()
    print(f"После процентов: {account.balance}")

def demo_state_management():
    print_separator("4. УПРАВЛЕНИЕ СОСТОЯНИЕМ")
    account = BankAccount("ACC004", "Елена Козлова", 0, 1000, 5.0)
    print(f"Активен: {account.is_active}")
    account.close_account()
    print(f"После закрытия: {account.is_active}")
    try:
        account.deposit(500)
    except ValueError as e: 
        print(f"Ошибка: {e}")
    account.activate_account()
    account.deposit(500)
    print(f"После активации и пополнения: {account.balance}")

def demo_validation():
    print_separator("5. ВАЛИДАЦИЯ")
    try:
        BankAccount("ACC005", "Тест Тестов", "сто рублей", 0, 5)
    except TypeError as e:
        print(f"Ошибка типа: {e}")
    try:
        BankAccount("ACC006", "", 1000, 0, 5)
    except ValueError as e:
        print(f"Ошибка значения: {e}")

def demo_comparison():
    print_separator("6. СРАВНЕНИЕ ОБЪЕКТОВ")
    acc1 = BankAccount("ACC009", "Анна Каренина", 10000, 5000, 4.5)
    acc2 = BankAccount("ACC009", "Анна Каренина", 5000, 2000, 3.0)
    acc3 = BankAccount("ACC010", "Константин Левин", 7500, 3000, 4.0)
    print(f"acc1 == acc2: {acc1 == acc2}")
    print(f"acc1 == acc3: {acc1 == acc3}")

def demo_advanced_scenarios():
    print_separator("7. СЛОЖНЫЕ СЦЕНАРИИ")
    credit_account = BankAccount("CR001", "Бизнес Клиент", 1000, 10000, 12.5)
    credit_account.withdraw(8000)
    print(f"Баланс после снятия: {credit_account.balance}")
    credit_account.apply_interest()
    print(f"После процентов: {credit_account.balance}")
    
    active_account = BankAccount("CR002", "Осторожный Клиент", 5000, 0, 5.0)
    try:
        active_account.close_account()
    except ValueError as e:
        print(f"Ошибка при закрытии: {e}")

def main():
    print("="*60)
    print("     ДЕМОНСТРАЦИЯ КЛАССА BankAccount")
    print("="*60)
    demo_basic_operations()
    demo_properties_and_setters()
    demo_business_methods()
    demo_state_management()
    demo_validation()
    demo_comparison()
    demo_advanced_scenarios()
    print_separator("ИТОГИ")
    print(f"Всего создано счетов: {BankAccount.total_accounts}")

if __name__ == "__main__":
    main()