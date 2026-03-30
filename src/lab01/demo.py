from model import BankAccount, SavingsAccount, BusinessAccount

def print_block(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

def main():
    print_block("СЦЕНАРИЙ 1: СОЗДАНИЕ ОБЪЕКТОВ И НАСЛЕДОВАНИЕ")
    
    mark = BankAccount("ACC-001", "Марк", balance=1000.0)
    matvey = SavingsAccount("SAV-001", "Матвей", balance=5000.0, interest_rate=10.0)
    roman = BusinessAccount("BIZ-001", "Роман", balance=10000.0, tax_id="7701")

    print(f"Создан базовый счет: {mark}")
    print(f"Создан сберегательный: {matvey}")
    print(f"Создан бизнес-счет: {roman}")

    print_block("СЦЕНАРИЙ 2: ПОЛИМОРФИЗМ (ОБЩИЙ ИНТЕРФЕЙС)")
    bank_database = [mark, matvey, roman]

    for acc in bank_database:
        bonus = acc.calculate_annual_bonus()
        print(f" > Клиент: {acc.owner_name:10} | Бонус: {bonus:>8.2f} руб.")

    print_block("СЦЕНАРИЙ 3: УНИКАЛЬНЫЕ МЕТОДЫ ДОЧЕРНИХ КЛАССОВ")
    
    print(f"Баланс Матвея до процентов: {matvey.balance}")
    matvey.apply_interest()
    print(f"Баланс Матвея после процентов: {matvey.balance}")

    print(f"\nБаланс Романа до комиссии: {roman.balance}")
    roman.pay_service_fee()
    print(f"Баланс Романа после комиссии: {roman.balance}")

    print_block("СЦЕНАРИЙ 4: ПРОВЕРКА ТИПОВ И ФИЛЬТРАЦИЯ (ISINSTANCE)")
    
    for acc in bank_database:
        if isinstance(acc, BusinessAccount):
            print(f" - Найден Бизнес: {acc.owner_name}, ИНН: {acc._tax_id}")

    print_block("СЦЕНАРИЙ 5: ПРОВЕРКА ВАЛИДАЦИИ И ОГРАНИЧЕНИЙ")
    
    try:
        mark.deposit(-500)
    except ValueError as e:
        print(f"Поймана ошибка: {e}")

    try:
        roman.withdraw(200000)
    except ValueError as e:
        print(f"Поймана ошибка: {e}")

    print_block("СЦЕНАРИЙ 6: ИСТОРИЯ ТРАНЗАКЦИЙ")
    print(f"История для {matvey.owner_name}:")
    for i, t in enumerate(matvey.transactions, 1):
        print(f" {i}. {t['date']} | {t['type']:10} | {t['amount']:>8.2f} | {t['description']}")

    print_block("СЦЕНАРИЙ 7: СТАТИСТИКА КЛАССА")
    total = BankAccount.get_total_accounts()
    print(f"Всего объектов в системе: {total}")

if __name__ == "__main__":
    main()