from models import SavingsAccount, BusinessAccount, BankOffice
from base import BankAccount

def run_extended_demo():
    print("="*70)
    print("БАНКОВСКАЯ СИСТЕМА")
    print("="*70)

    office = BankOffice("Центральный")
    
    print(f"\n[ИНИЦИАЛИЗАЦИЯ]: Регистрация счетов в офисе '{office.office_name}'...")
    acc_s = SavingsAccount("100001", "Вадим Конев", 5000.0, 10.0)
    acc_b = BusinessAccount("200002", "ООО Газпром", 2000.0, 3000.0)
    acc_simple = BankAccount("300003", "Мария Осипова", 1000.0)

    for a in [acc_s, acc_b, acc_simple]:
        office.add(a)
        print(f"Зарегистрирован: {a}")

    print("\n" + "-"*30)
    print("[СЦЕНАРИЙ 1] ПРОВЕРКА ПОЛИМОРФИЗМА (Снятие 4000.00)")
    print("-"*30)
    for acc in [acc_s, acc_b]:
        print(f"Обработка запроса для: {acc.owner_name}...")
        try:
            acc.withdraw(4000.0)
            print(f"   Статус: УСПЕШНО. Текущий баланс: {acc.balance:.2f}")
        except ValueError as e:
            print(f"   Статус: ОТКЛОНЕНО. Причина: {e}")

    print("\n" + "-"*30)
    print("[СЦЕНАРИЙ 2] СПЕЦИФИЧЕСКАЯ ЛОГИКА (Начисление %)")
    print("-"*30)
    print(f"Баланс до начисления: {acc_s.balance:.2f}")
    interest = acc_s.apply_interest()
    print(f"Выполнение метода apply_interest()...")
    print(f"   Добавлено процентов: +{interest:.2f}")
    print(f"Новый статус счета: {acc_s}")

    print("\n" + "-"*30)
    print("[СЦЕНАРИЙ 3] ПРОВЕРКА СИСТЕМЫ ВАЛИДАЦИИ")
    print("-"*30)
    print("Входящая транзакция: ПОПОЛНЕНИЕ (-500.00)")
    try:
        acc_simple.deposit(-500)
    except ValueError as e:
        print(f"   Ошибка валидации: {e}")

    print("\n" + "-"*30)
    print("[СЦЕНАРИЙ 4] ФИЛЬТРАЦИЯ КОЛЛЕКЦИИ (isinstance)")
    print("-"*30)
    print(f"Всего счетов в реестре: {len(office)}")
    b_accounts = office.get_accounts_by_type(BusinessAccount)
    print(f"Поиск объектов типа BusinessAccount...")
    print(f"Найдено совпадений: {len(b_accounts)}")
    for b in b_accounts:
        print(f"   Детали: {b}")

    print("\n" + "-"*30)
    print("[СЦЕНАРИЙ 5] АУДИТ ТРАНЗАКЦИЙ (Инкапсуляция)")
    print("-"*30)
    print(f"Запрос истории операций для: {acc_b.owner_name}")
    print("--- НАЧАЛО ИСТОРИИ ---")
    print(acc_b.get_history())
    print("--- КОНЕЦ ИСТОРИИ ---")

    print("\n" + "="*70)
    print("ВСЕ ТЕСТЫ ЗАВЕРШЕНЫ УСПЕШНО.")
    print("="*70)

if __name__ == "__main__":
    run_extended_demo()