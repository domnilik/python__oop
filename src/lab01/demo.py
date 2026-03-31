from model import BankAccount

def print_block(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

def run_demo():
   
    acc_m = BankAccount("101", "Марк", 1500.0, "Обычный")
    acc_v = BankAccount("102", "Матвей", 1500.0, "Сберегательный")

    print_block("СЦЕНАРИЙ 1: СОЗДАНИЕ ОБЪЕКТА И ВЫВОД")
   
    print(f"Объект 1 (дружелюбный вывод): {acc_m}")
    print(f"Объект 2 (отладочный вывод): {repr(acc_v)}")
    
    print(f"Тип счета Матвея: {acc_v._account_type}, ставка: {acc_v._interest_rate}%")

    print_block("СЦЕНАРИЙ 2: СРАВНЕНИЕ ОБЪЕКТОВ")
    
    print(f"Счет Марка ({acc_m.balance}) и Матвея ({acc_v.balance})")
    print(f"Результат сравнения (==): {acc_m == acc_v}")
    
    print("\nИзменяем баланс Марка...")
    acc_m.deposit(500)
    print(f"Теперь счета равны? {acc_m == acc_v}")

    print_block("СЦЕНАРИЙ 3: ИЗМЕНЕНИЕ ДАННЫХ ЧЕРЕЗ SETTER")
    print(f"Текущий владелец: {acc_m.owner_name}")
    
    acc_m.owner_name = "марк аврелий"
    print(f"Новый владелец (после обработки): {acc_m.owner_name}")

    print_block("СЦЕНАРИЙ 4: ДОСТУП К АТРИБУТАМ КЛАССА")
  
    print(f"Всего создано счетов (через класс): {BankAccount.total_accounts}")
    print(f"Доступ через экземпляр Марка: {acc_m.total_accounts}")
    
    print("\nСоздаем еще один технический счет...")
    temp_acc = BankAccount("999", "Технический Счет", 0.0)
    print(f"Обновленное количество счетов: {BankAccount.total_accounts}")

    print_block("СЦЕНАРИЙ 5: СОСТОЯНИЕ ОБЪЕКТА И ОГРАНИЧЕНИЯ")
    
    status_now = "Активен" if acc_m.is_active else "Закрыт"
    print(f"Аккаунт Марка сейчас: {status_now}")
    
    print("Выполняем закрытие счета...")
    acc_m.close_account()
    
    print(f"Статус после close_account(): {'Активен' if acc_m.is_active else 'Закрыт'}")
    
    try:
        print("Попытка финансовой операции на закрытом счету:")
        acc_m.deposit(500)
    except ValueError as e:
        print(f"Блокировка сработала корректно: {e}")

    print_block("СЦЕНАРИЙ 6: ПРОВЕРКА ВАЛИДАЦИИ (TRY/EXCEPT)")
 
    test_cases = [
        {"name": "Иван123", "num": "777", "bal": 100, "msg": "Имя с цифрами"},
        {"name": "Олег", "num": "12", "bal": 100, "msg": "Короткий номер счета"},
        {"name": "Анна", "num": "888", "bal": -50000, "msg": "Критический минус"}
    ]
    
    for case in test_cases:
        try:
            print(f"Тест: {case['msg']} ({case['name']})...")
            BankAccount(case['num'], case['name'], case['bal'])
        except (ValueError, TypeError) as e:
            print(f"Результат: {e}")

   
    print_block("ИТОГОВАЯ ИСТОРИЯ ОПЕРАЦИЙ (МАТВЕЙ)")
    acc_v.apply_interest()
    acc_v.deposit(1000)
    print(acc_v.get_history())

    print("\n" + "=" * 60)
    print("ПОЛНЫЙ ЦИКЛ ТЕСТИРОВАНИЯ ЗАВЕРШЕН")
    print("=" * 60)

if __name__ == "__main__":
    run_demo()