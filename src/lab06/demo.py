from container import TypedCollection, Displayable, Scorable

class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner: str = owner
        self.balance: float = balance

    def get_info(self) -> str:
        return f"Счет: {self.owner}, Баланс: {self.balance:.2f}"

    def get_score(self) -> float:
        return self.balance

def run_demo():
    print("=== ЛР-6: Generics, Typing и Protocols ===\n")

    # --- Подготовка данных ---
    office: TypedCollection[BankAccount] = TypedCollection()
    office.add(BankAccount("Марк", 15000.0))
    office.add(BankAccount("Павел", 5000.0))
    office.add(BankAccount("Ольга", 2100.0))

    # --- Сценарий 1. Тест find  ---
    print("--- Сценарий 1. Тест find ---")
    rich = office.find(lambda x: x.balance > 10000)
    if rich:
        print(f"Найден богатый клиент: {rich.owner}")
    
    poor = office.find(lambda x: x.balance > 100000)
    if not poor:
        print(f"Поиск (баланс > 100000): Результат None (как и ожидалось)")

    # --- Тест filter  ---
    print("\n--- Тест filter ---")
    filtered = office.filter(lambda x: x.balance > 3000)
    for acc in filtered:
        print(acc.get_info())

    # --- Тест map ---
    print("\n--- Сценарий 2. Тест map ---")
    names = office.map(lambda x: x.owner.upper())
    print(f"Тип результата: {type(names).__name__} содержащий {type(names[0]).__name__}")
    print(f"Список имен: {names}")

    # --- Тест Protocols: Сценарий 1 (Displayable) ---
    print("\n--- Тест Protocols (Displayable) - Сценарий 3 ---")
    display_box: TypedCollection[Displayable] = TypedCollection()
    display_box.add(BankAccount("Дарья", 500.0))
    
    for item in display_box.get_all():
        print(f"Отображение через протокол: {item.get_info()}")

    # --- Тест Protocols: Сценарий 2 (Scorable) ---
    print("\n--- Тест Protocols (Scorable) ---")
    score_box: TypedCollection[Scorable] = TypedCollection()# Демонстрация того, что один и тот же класс TypedCollection работает с разными TypeVar
    score_box.add(BankAccount("Игорь", 300.0))
    
    for item in score_box.get_all(): # Вызов метода протокола score (в нашем случае get_score)
        print(f"Показатель (score) через протокол: {item.get_score()}")

if __name__ == "__main__":
    run_demo()