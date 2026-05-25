from app import BankApplication
from exceptions import ItemNotFoundError, DuplicateItemError, ValidationError

class BankCLI:
    """Консольный интерфейс пользователя (CLI)."""

    def __init__(self, app: BankApplication):
        self.app = app

    def print_menu(self) -> None:
        """Вывести интерактивное меню."""
        print("\n=== МЕНЮ УПРАВЛЕНИЯ БАНКОМ ===")
        print("1. Показать все счета")
        print("2. Добавить новый счет")
        print("3. Удалить счет")
        print("4. Найти счет")
        print("5. Сортировка счетов")
        print("6. Фильтрация по балансу")
        print("0. Выход")

    def show_all(self) -> None:
        """Вывести счета в виде таблицы."""
        accounts = self.app.get_all_accounts()
        if not accounts:
            print("\n[База данных пуста]")
            return
        print(f"\n{'№ Счета':<10} | {'Владелец':<12} | {'Баланс':<10} | {'Тип счета'}")
        print("-" * 55)
        for acc in accounts:
            print(acc)

    def add_item(self) -> None:
        """Интерфейс добавления элемента с валидацией ввода."""
        try:
            acc_num = input("Введите номер счета: ").strip()
            owner = input("Введите имя владельца: ").strip()
            balance_raw = input("Введите начальный баланс: ").strip()
            acc_type = input("Введите тип (Сберегательный/Обычный/Бизнес): ").strip()

            if not acc_num or not owner or not balance_raw or not acc_type:
                print("\n[Ошибка]: Все поля обязательны для заполнения!")
                return

            self.app.add_account(acc_num, owner, balance_raw, acc_type)
            print("\nУспех: Счет успешно добавлен!")
        except ValidationError as e:
            print(f"\n[Ошибка валидации]: {e}")
        except DuplicateItemError as e:
            print(f"\n[Ошибка бизнес-логики]: {e}")

    def delete_item(self) -> None:
        """Интерфейс удаления с подтверждением операции."""
        acc_num = input("Введите номер счета для удаления: ").strip()
        
        try:
           
            acc_info = self.app.find_account(acc_num)
            
          
            confirm = input(f"Удалить \"{acc_info}\"? (y/n): ").strip().lower()
            if confirm != 'y':
                print("Операция отменена.")
                return
                
            self.app.delete_account(acc_num)
            print("Успех: Счет успешно удален.")
            
        except (ItemNotFoundError, ValidationError) as e:
            print(f"\n[Ошибка]: {e}")

    def sort_items(self) -> None:
        """Интерфейс выбора стратегии сортировки."""
        print("\nСортировать по:")
        print("1. Имени владельца")
        print("2. Балансу")
        print("3. Типу счета")
        try:
            choice = int(input("Выберите стратегию: "))
            if choice in [1, 2, 3]:
                self.app.sort_accounts(choice)
                print("Успех: Коллекция отсортирована.")
                self.show_all()
            else:
                print("Неверный вариант сортировки.")
        except ValueError:
            print("Ошибка: Введите число от 1 до 3.")

    def filter_items(self) -> None:
        """Интерфейс фильтрации."""
        try:
            min_balance = input("Показать счета с балансом от: ").strip()
            filtered = self.app.filter_accounts(min_balance)
            if not filtered:
                print("Счетов с таким балансом не найдено.")
                return
            print(f"\nРезультаты фильтрации:")
            for acc in filtered:
                print(acc)
        except ValidationError as e:
            print(f"\n[Ошибка валидации]: {e}")

    def run(self) -> None:
        """Главный цикл интерактивного меню CLI."""
        self.app.load_data()
        while True:
            self.print_menu()
            try:
                choice = int(input("\nВыберите пункт меню: "))
                if choice == 1:
                    self.show_all()
                elif choice == 2:
                    self.add_item()
                elif choice == 3:
                    self.delete_item()
                elif choice == 4:
                    self.find_item()
                elif choice == 5:
                    self.sort_items()
                elif choice == 6:
                    self.filter_items()
                elif choice == 0:
                    print("Сохранение данных и завершение работы...")
                    self.app.save_data()
                    print("До свидания!")
                    break
                else:
                    print("Ошибка: Выберите существующий пункт меню (0-6).")
            except ValueError:
                print("Ошибка ввода: введите число!")