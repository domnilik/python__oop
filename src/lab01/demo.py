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