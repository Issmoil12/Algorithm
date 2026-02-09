#первое задание

number = int(input("Введите целое число: "))

while number <= 0:
    number = int(input("Число должно быть положительным. Повторите ввод: "))

print("Корректное число:", number)

#второе задание

while True:
    number = int(input("Введите число: "))
    if number > 100:
        break

print("Введено число больше 100:", number)

#третье задание

n = int(input("Введите n: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Сумма чисел от 1 до", n, "равна", total)

#четвертое задание

for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end=" ")
    print()

#пятое задание

i = 1
while i <= 10:
    print(i)
    i += 1
