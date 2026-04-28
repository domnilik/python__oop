from models import SavingsAccount, BusinessAccount
from interfaces import Printable, Comparable

def get_priority_account(acc_a: Comparable, acc_b: Comparable) -> Comparable:
    if acc_a.compare_to(acc_b) > 0:
        return acc_a
    return acc_b

def run_demo():
    print("="*60)
    print("Лабораторная работа №4: Банковская система (Интерфейсы)")
    print("="*60)

    
    print("\n--- Сценарий 1: Создание объектов и полиморфизм ---")
    print("Создание банковских счетов разных типов...")
    acc1 = SavingsAccount("101", "Вадим Конев", 15000.0, 10.5)
    acc2 = BusinessAccount("202", "ООО Вектор", 5000.0, 50000.0)
    acc3 = SavingsAccount("303", "Анна Сидорова", 25000.0, 8.0)
    
    print("\n[Данные о счетах (через Printable)]")
    storage: list[Printable] = [acc1, acc2, acc3]
    for item in storage:
        print(item.to_string())

    
    print("\n--- Сценарий 2: Работа через интерфейсы ---")
    print("Поиск счета с наибольшим балансом через Comparable...")
    best = get_priority_account(acc1, acc3)
    print(f"Результат сравнения: {best.to_string()}")

    print("\n[Проверка реализации интерфейсов через isinstance()]")
    for obj in [acc1, acc2]:
        p = isinstance(obj, Printable)
        c = isinstance(obj, Comparable)
        print(f"{obj.__class__.__name__}: Printable={p}, Comparable={c}")

    
    print("\n--- Сценарий 3: Сортировка коллекции ---")
    print("Сортировка счетов по балансу (от большего к меньшему):")
    accounts = [acc1, acc2, acc3]
    accounts.sort(key=lambda x: x.balance, reverse=True)
    for acc in accounts:
        print(f"Баланс: {acc.balance:8.2f} | {acc.to_string()}")


    print("\n--- Сценарий 4: Фильтрация по интерфейсу ---")
    print("Обработка смешанных данных (фильтрация только Printable объектов):")
    raw_data = [acc1, "Некорректные данные", acc2, 12345, acc3]
    for obj in raw_data:
        if isinstance(obj, Printable):
            print(f"[Ok] Валидный объект: {obj.to_string()}")
        else:
            print(f"[Skip] Пропущен объект типа {type(obj).__name__}")

    print("\n" + "="*60)
    print("Демонстрация завершена")
    print("="*60)

if __name__ == "__main__":
    run_demo()