def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        return str(a) + str(b)

# Примеры использования
print(add_everything_up(123.456, 'строка'))  # 123.456строка
