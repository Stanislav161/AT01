def safe_modulo(a, b):
    """
    Возвращает остаток от деления a на b.
    Если b == 0, выбрасывает исключение ZeroDivisionError.
    """
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return a % b