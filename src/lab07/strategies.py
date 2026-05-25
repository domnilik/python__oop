def by_owner(account):
    """Сортировка по имени владельца."""
    return account.owner_name

def by_balance(account):
    """Сортировка по балансу."""
    return account.balance

def is_active(account):
    """Фильтр активных счетов."""
    return account.is_active

def limit_filter(min_amount):
    """Фабрика фильтров по минимальной сумме."""
    def filter_fn(account):
        return account.balance >= min_amount
    return filter_fn

class InterestStrategy:
    """Callable-стратегия для начисления бонуса."""
    def __init__(self, bonus_percent=1.0):
        self.bonus_percent = bonus_percent

    def __call__(self, account):
        if account.is_active:
            bonus = account.balance * (self.bonus_percent / 100)
            account.deposit(bonus)
            return bonus
        return 0