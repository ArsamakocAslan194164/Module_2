n = int(input("Введите число от 3 до 20: "))
i = ""

for i in range(1, n):
    for j in range(i + 1, n + 1):
        if n % (i + j) == 0:
            i += f"{i}{j}"

print("Нужный пароль:", i)