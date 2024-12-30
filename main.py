# Домашнее задание по теме "Try и Except"


def add_everything_up(a, b):
    # Проверяем, являются ли оба аргумента числовыми
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b  # Суммируем, если оба числа
    elif isinstance(a, str) and isinstance(b, str):
        return a + b  # Конкатенируем, если обе строки
    else:
        # Если один аргумент число, а другой строка
        return str(a) + str(b)  # Возвращаем их строковое представление

# Примеры использования функции
print(add_everything_up(123.456, 'строка'))  # '123.456строка'
print(add_everything_up('яблоко', 4215))     # 'яблоко4215'
print(add_everything_up(123.456, 7))          # 130.456



