def validate_balance(value):
    if not isinstance(value, (int, float)):
        raise TypeError(f"Баланс должен быть числом")
    if value < 0:
        raise ValueError(f"Баланс не может быть отрицательным: {value}")
    return float(value)

def validate_credit_limit(value):
    if not isinstance(value, (int, float)):
        raise TypeError(f"Кредитный лимит должен быть числом")
    if value < 0:
        raise ValueError(f"Кредитный лимит не может быть отрицательным: {value}")
    return float(value)

def validate_interest_rate(value):
    if not isinstance(value, (int, float)):
        raise TypeError(f"Процентная ставка должна быть числом")
    if not (0 <= value <= 100):
        raise ValueError(f"Процентная ставка должна быть от 0 до 100, получена {value}")
    return float(value)

def validate_account_number(value):
    if not isinstance(value, str):
        raise TypeError(f"Номер счета должен быть строкой")
    value = value.strip()
    if not value or len(value) < 5:
        raise ValueError("Номер счета должен содержать минимум 5 символов")
    return value

def validate_owner_name(value):
    if not isinstance(value, str):
        raise TypeError(f"Имя владельца должно быть строкой")
    value = value.strip()
    if not value or len(value) < 2:
        raise ValueError("Имя владельца должно содержать минимум 2 символа")
    return value