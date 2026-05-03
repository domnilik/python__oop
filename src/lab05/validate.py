import re

def validate_account_number(number):
    """Проверка номера счета на соответствие формату."""
    if not isinstance(number, (str, int)):
        raise TypeError(f"Тип данных {type(number)} недопустим для номера счета!")
    
    str_number = str(number).strip()
    
   
    if not re.fullmatch(r'\d{3,20}', str_number):
        if not str_number.isdigit():
            raise ValueError(f"Критическая ошибка: Номер счета '{str_number}' содержит недопустимые символы!")
        if len(str_number) < 3:
            raise ValueError(f"Ошибка: Номер счета {str_number} слишком короткий (минимум 3 цифры).")
        if len(str_number) > 20:
            raise ValueError(f"Ошибка: Номер счета слишком длинный (максимум 20 цифр).")
            
    return str_number

def validate_owner_name(name):
    """Валидация ФИО владельца счета."""
    if not isinstance(name, str):
        raise TypeError("Имя владельца должно быть строковой переменной!")
    
    
    clean_name = " ".join(name.split())
    
    if len(clean_name) < 2:
        raise ValueError(f"Ошибка: Имя '{clean_name}' слишком короткое (мин. 2 символа)!")
    
    
    if not re.match(r'^[a-zA-Zа-яА-ЯёЁ\s-]+$', clean_name):
        if any(char.isdigit() for char in clean_name):
            raise ValueError(f"Ошибка: В имени '{clean_name}' обнаружены цифры!")
        raise ValueError(f"Ошибка: В имени '{clean_name}' обнаружены недопустимые спецсимволы!")
        
    return clean_name.title()  

def validate_balance(balance):
    """Базовая проверка числового значения баланса."""
    try:
        val = float(balance)
    except (ValueError, TypeError):
        raise TypeError(f"Значение '{balance}' должно быть числом (int или float)!")
        
    if val < -10000.0: 
        raise ValueError(f"Нарушение ограничений: Баланс не может быть ниже -10000.0 ({val})!")
        
    return val

def validate_amount(amount):
    """Валидация суммы для проведения операции (пополнение/снятие)."""
    try:
        val = float(amount)
    except (ValueError, TypeError):
        raise TypeError(f"Сумма операции '{amount}' должна быть числом!")
        
    if val <= 0:
        raise ValueError(f"Ошибка: Сумма операции должна быть строго больше нуля (передано: {val})!")
    
    
    if val > 1_000_000:
        raise ValueError("Ошибка: Превышен лимит разовой операции (макс: 1 000 000)!")
        
    return round(val, 2) 