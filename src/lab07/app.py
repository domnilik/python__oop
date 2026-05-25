from typing import List, Any
from collection import BankOffice
from model import BankAccount, SavingsAccount, CheckingAccount
import strategies as st
from exceptions import ItemNotFoundError, DuplicateItemError, ValidationError
from validate import validate_account_number, validate_owner_name, validate_balance

class BankApplication:

    def __init__(self, storage_path: str):
        self.storage_path = storage_path
        self.office = BankOffice("Центральный Офис")

    def load_data(self) -> None:
        from storage import load
        data = load(self.storage_path)
        for item in data:
            try:
                num = validate_account_number(item["account_number"])
                owner = validate_owner_name(item["owner_name"])
                balance = validate_balance(item["balance"])
                acc_type = item["account_type"]

                # Передаем аргументы в правильном порядке согласно новой модели
                if "сбер" in acc_type.lower() or "Savings" in acc_type:
                    acc = SavingsAccount(owner, balance, 0.1, num)
                elif "расч" in acc_type.lower() or "Checking" in acc_type:
                    acc = CheckingAccount(owner, balance, 5000.0, num)
                else:
                    acc = BankAccount(num, owner, balance, acc_type)

                self.office.add(acc)
            except (ValidationError, ValueError):
                continue

    def save_data(self) -> None:
        from storage import save
        raw_data = []
        for acc in self.office._items:
            raw_data.append({
                "account_number": acc.account_number,
                "owner_name": acc.owner,
                "balance": acc.balance,
                "account_type": acc.account_type
            })
        save(raw_data, self.storage_path)

    def get_all_accounts(self) -> List[str]:
        return [str(acc) for acc in self.office._items]

    def add_account(self, acc_num: str, owner: str, balance_raw: Any, acc_type: str) -> None:
        valid_num = validate_account_number(acc_num)
        valid_owner = validate_owner_name(owner)
        valid_balance = validate_balance(balance_raw)
        
        for acc in self.office._items:
            if acc.account_number == valid_num:
                raise DuplicateItemError(f"Счет с номером {valid_num} уже существует!")
        
        t_clean = acc_type.strip().lower()
        # Создаем объекты с учетом нового порядка параметров
        if t_clean in ["сберегательный", "1"]:
            new_acc = SavingsAccount(valid_owner, valid_balance, 0.1, valid_num)
        elif t_clean in ["расчетный", "2", "бизнес"]:
            new_acc = CheckingAccount(valid_owner, valid_balance, 5000.0, valid_num)
        else:
            new_acc = BankAccount(valid_num, valid_owner, valid_balance, "Обычный")

        self.office.add(new_acc)

    def get_account_owner_name(self, acc_num: str) -> str:
        valid_num = validate_account_number(acc_num)
        for acc in self.office._items:
            if acc.account_number == valid_num:
                return acc.owner
        raise ItemNotFoundError(f"Счет №{valid_num} не найден!")

    def delete_account(self, acc_num: str) -> None:
        valid_num = validate_account_number(acc_num)
        for i, acc in enumerate(self.office._items):
            if acc.account_number == valid_num:
                self.office._items.pop(i)
                return
        raise ItemNotFoundError(f"Счет №{valid_num} не найден!")

    def find_account(self, acc_num: str) -> str:
        valid_num = validate_account_number(acc_num)
        for acc in self.office._items:
            if acc.account_number == valid_num:
                return str(acc)
        raise ItemNotFoundError(f"Счет №{valid_num} не найден!")

    def sort_accounts(self, criteria: int) -> None:
        if criteria == 1:
            self.office.sort_by(st.by_owner)
        elif criteria == 2:
            self.office.sort_by(st.by_balance)
        elif criteria == 3:
            self.office.sort_by(lambda acc: acc.account_type)

    def filter_accounts(self, min_balance: Any) -> List[str]:
        valid_min = validate_balance(min_balance)
        predicate = st.limit_filter(valid_min)
        filtered_office = self.office.filter_by(predicate)
        return [str(acc) for acc in filtered_office._items]