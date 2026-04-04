from model import BankAccount
from collection import BankOffice

def run_lab02_demo():
    office = BankOffice("Главный Офис")
    

    acc1 = BankAccount("101", "Марк", 5000.0, "Сберегательный")
    acc2 = BankAccount("102", "Матвей", 3000.0, "Обычный")
    acc3 = BankAccount("103", "Анна", 10000.0, "Бизнес")
    
    office.add(acc1)
    office.add(acc2)
    office.add(acc3)
    
    print(f"--- Создана коллекция ---")
    print(office)

   
    print(f"\n--- Тест защиты ---")
    try:
        office.add(BankAccount("101", "Дубликат", 100))
    except ValueError as e:
        print(f"Ошибка дубликата: {e}")

    
    print(f"\n--- Магические методы ---")
    print(f"Количество счетов: {len(office)}")
    for acc in office:
        print(f"Счет: {acc}")

    
    print(f"\n--- Поиск и индексация ---")
    print(f"Элемент по индексу [0]: {office[0]}")
    print(f"Поиск номера 102: {office.find_by_number('102')}")

  
    print(f"\n--- Сортировка по балансу (DESC) ---")
    office.sort_by_balance(reverse=True)
    for acc in office:
        print(f"{acc.balance} руб. | {acc.owner_name}")

    
    print(f"\n--- Фильтрация активных ---")
    office.find_by_number("103").close_account()
    active_only = office.get_active_accounts()
    print(f"Всего: {len(office)}, Активных: {len(active_only)}")
    for acc in active_only:
        print(f"Активен: {acc}")

  
    print(f"\n--- Удаление ---")
    office.remove_at(0)
    print(f"Осталось после удаления: {len(office)}")

if __name__ == "__main__":
    run_lab02_demo()