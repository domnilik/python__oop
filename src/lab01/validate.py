def validate_balance(value):
    if not isinstance(value, (int, float)):
        raise TypeError(f"Баланс должен быть числом, получен {type(value).__name__}")
    if value < 0:
        raise ValueError(f"Баланс не может быть отрицательным: {value}")
    return True

def validate_credit_limit(value):
    if not isinstance(value, (int, float)):
        raise TypeError(f"Кредитный лимит должен быть числом, получен {type(value).__name__}")
    if value < 0:
        raise ValueError(f"Кредитный лимит не может быть отрицательным: {value}")
    return True

def validate_interest_rate(value):
    if not isinstance(value, (int, float)):
        raise TypeError(f"Процентная ставка должна быть числом, получен {type(value).__name__}")
    if value < 0 or value > 100:
        raise ValueError(f"Процентная ставка должна быть от 0 до 100, получена {value}")
    return True

def validate_account_number(value):
    if not isinstance(value, str):
        raise TypeError(f"Номер счета должен быть строкой, получен {type(value).__name__}")
    if not value.strip():
        raise ValueError("Номер счета не может быть пустым")
    if len(value.strip()) < 5:
        raise ValueError(f"Номер счета должен содержать минимум 5 символов, получено {len(value)}")
    return True

def validate_owner_name(value):
    if not isinstance(value, str):
        raise TypeError(f"Имя владельца должно быть строкой, получен {type(value).__name__}")
    if not value.strip():
        raise ValueError("Имя владельца не может быть пустым")
    if len(value.strip()) < 2:
        raise ValueError(f"Имя владельца должно содержать минимум 2 символа, получено {len(value)}")
    return True

def validate_withdrawal(balance, amount, credit_limit=0):
    if not isinstance(amount, (int, float)):
        raise TypeError(f"Сумма должна быть числом, получена {type(amount).__name__}")
    if amount <= 0:
        raise ValueError(f"Сумма для снятия должна быть положительной: {amount}")
    available_funds = balance + credit_limit
    if amount > available_funds:
        raise ValueError(f"Недостаточно средств. Доступно: {available_funds:.2f}, запрошено: {amount:.2f}")
    return True
