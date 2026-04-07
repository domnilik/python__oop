from model import BankAccount
from collection import BankOffice

def print_scenario(number, title):
    """Вспомогательная функция для красивого вывода заголовков"""
    print(f"\n{'='*60}")
    print(f"СЦЕНАРИЙ {number}: {title.upper()}")
    print(f"{'='*60}")

def run_lab02_demo():
    # Инициализация офиса
    office = BankOffice("Центральный филиал")
    
    # СЦЕНАРИЙ 1
    print_scenario(1, "Создание объектов и наполнение коллекции")
    acc1 = BankAccount("101", "Марк", 5000.0, "Сберегательный")
    acc2 = BankAccount("102", "Матвей", 3000.0, "Обычный")
    acc3 = BankAccount("103", "Анна", 10000.0, "Бизнес")
    
    office.add(acc1)
    office.add(acc2)
    office.add(acc3)
    print(f"Успешно создано и добавлено {len(office)} счетов.")
    print(f"Текущее состояние: {office}")

    # СЦЕНАРИЙ 2
    print_scenario(2, "Тест защиты (Дубликаты и Типы)")
    try:
        print("Попытка добавить счет с существующим номером 101...")
        office.add(BankAccount("101", "Клон", 100.0))
    except ValueError as e:
        print(f"Ожидаемая ошибка: {e}")
    
    try:
        print("\nПопытка добавить некорректный тип данных (строку)...")
        office.add("Не счет")
    except TypeError as e:
        print(f"Ожидаемая ошибка: {e}")

    # СЦЕНАРИЙ 3
    print_scenario(3, "Магические методы (__len__, __iter__)")
    print(f"Количество элементов через len(): {len(office)}")
    print("Перебор всей коллекции через цикл for:")
    for acc in office:
        print(f"  -> {acc}")

    # СЦЕНАРИЙ 4
    print_scenario(4, "Поиск и индексация (__getitem__)")
    print(f"Прямой доступ к office[0]: {office[0]}")
    
    search_id = "102"
    found = office.find_by_number(search_id)
    print(f"Результат поиска счета {search_id}: {found if found else 'Не найден'}")

    # СЦЕНАРИЙ 5
    print_scenario(5, "Сортировка и фильтрация")
    print("1. Сортировка по убыванию баланса:")
    office.sort_by_balance(reverse=True)
    for acc in office:
        print(f"   {acc.balance:>8} руб. | {acc.owner_name}")
    
    print("\n2. Фильтрация (создание новой коллекции активных счетов):")
    # Закрываем один счет для теста фильтра
    office.find_by_number("103").close_account()
    
    active_office = office.get_active_accounts()
    print(f"Всего счетов: {len(office)}")
    print(f"Активных счетов в НОВОЙ коллекции: {len(active_office)}")
    for acc in active_office:
        print(f"   [АКТИВЕН] {acc}")

    # СЦЕНАРИЙ 6 
    print_scenario(6, "Удаление элементов")
    print(f"Удаляем первый элемент (индекс 0)...")
    removed = office.remove_at(0)
    print(f"Удален счет: {removed.owner_name}")
    print(f"Итого осталось в офисе: {len(office)}")

if __name__ == "__main__":
    run_lab02_demo()