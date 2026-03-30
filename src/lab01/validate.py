def validate_account_number(number):
    if not isinstance(number, str):
        number = str(number)
    if not number.isdigit():
        raise ValueError(f"Критическая ошибка: Номер счета '{number}' должен содержать только цифры!")
    if len(number) < 3:
        raise ValueError(f"Ошибка: Номер счета {number} слишком короткий (мин. 3 символа).")
    return number

def validate_owner_name(name):
    if not isinstance(name, str):
        raise TypeError("Имя владельца должно быть строкой!")
    clean_name = name.strip()
    if len(clean_name) < 2:
        raise ValueError(f"Ошибка: Имя '{clean_name}' слишком короткое!")
    if any(char.isdigit() for char in clean_name):
        raise ValueError(f"Ошибка: В имени '{clean_name}' обнаружены цифры!")
    return clean_name

def validate_balance(balance):
    try:
        val = float(balance)
    except (ValueError, TypeError):
        raise TypeError(f"Значение '{balance}' должно быть числом!")
    if val < 0:
        raise ValueError(f"Нарушение ограничений: Сумма не может быть отрицательной ({val})!")
    return val

def validate_amount(amount):
    val = validate_balance(amount)
    if val <= 0:
        raise ValueError("Ошибка: Сумма операции должна быть больше нуля!")
    return val