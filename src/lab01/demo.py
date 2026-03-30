from model import BankAccount

def print_block(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

def run_demo():
    acc_m = BankAccount("101", "Марк", 1500.0, "Обычный")
    acc_v = BankAccount("102", "Матвей", 1500.0, "Сберегательный")


    print_block("СЦЕНАРИЙ 1: СОЗДАНИЕ ОБЪЕКТА И ВЫВОД")
    print(f"Объект 1 (str): {acc_m}")
    print(f"Объект 2 (repr): {repr(acc_v)}")


    print_block("СЦЕНАРИЙ 2: СРАВНЕНИЕ ОБЪЕКТОВ")
    print(f"Счета Марка и Матвея равны по балансу? {acc_m == acc_v}")

    
    print_block("СЦЕНАРИЙ 3: ИЗМЕНЕНИЕ ДАННЫХ ЧЕРЕЗ SETTER")
    print(f"Текущий владелец: {acc_m.owner_name}")
    acc_m.owner_name = "Марк Аврелий"
    print(f"Новый владелец: {acc_m.owner_name}")

   
    print_block("СЦЕНАРИЙ 4: ДОСТУП К АТРИБУТАМ КЛАССА")
    print(f"Доступ через класс: {BankAccount.total_accounts}")
    print(f"Доступ через объект: {acc_m.total_accounts}")

   
    print_block("СЦЕНАРИЙ 5: СОСТОЯНИЕ ОБЪЕКТА И ОГРАНИЧЕНИЯ")
    status_now = "active" if acc_m._is_active else "closed"
    print(f"Текущий статус: {status_now}")
    
    acc_m.close_account()
    status_after = "closed" if not acc_m._is_active else "active"
    print(f"Статус после закрытия: {status_after}")
    
    try:
        acc_m.deposit(500)
    except ValueError as e:
        print(f"Ошибка при пополнении: {e}")

   
    print_block("СЦЕНАРИЙ 6: ПРОВЕРКА ВАЛИДАЦИИ (TRY/EXCEPT)")
    try:
        print("Попытка создать счет с некорректным именем...")
        bad_acc = BankAccount("777", "123", -10.0)
    except (ValueError, TypeError) as e:
        print(f"Ошибка валидации: {e}")

    print("\n" + "=" * 60)
    print("ТЕСТИРОВАНИЕ ЗАВЕРШЕНО")
    print("=" * 60)

if __name__ == "__main__":
    run_demo()