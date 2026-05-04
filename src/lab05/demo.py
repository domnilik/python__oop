from model import BankAccount
from collection import BankOffice
import strategies as st

office = BankOffice("Главный Офис")

accounts_data = [
    BankAccount("101", "Анна", 5000.0, "Сберегательный"),
    BankAccount("102", "Борис", 2000.0, "Обычный"),
    BankAccount("103", "Виктор", 15000.0, "Бизнес"),
    BankAccount("104", "Дарья", 500.0, "Обычный"),
    BankAccount("105", "Егор", 8000.0, "Сберегательный")
]

for acc in accounts_data:
    office.add(acc)

print("=== Исходное состояние  ===")
print(office)

print("\n=== Сценарий 1: Цепочка операций ===")
bonus_5 = st.InterestStrategy(bonus_percent=5.0)
result = (office
          .filter_by(st.limit_filter(1000))
          .sort_by(st.by_owner)
          .apply(bonus_5))
print(result)

print("\n=== Сценарий 2: Lambda и Map ===")
office.sort_by(lambda x: x.balance, reverse=True)
for summary in office.get_summaries():
    print(f"-> {summary}")

print("\n=== Сценарий 3: Callable-стратегия ===")
extra_bonus = st.InterestStrategy(bonus_percent=2.0)
office.apply(extra_bonus)
print(office)