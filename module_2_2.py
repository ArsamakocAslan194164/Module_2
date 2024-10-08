first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

if first == second == third:
    print(3)
elif first and second == third or third and second == first or first and third == first:
    print(2)
else:
    print(0)
