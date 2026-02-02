# 1)
a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))
c = int(input("Введите третье целое число: "))

average = (a + b + c) / 3

print("Среднее арифметическое:", average)
# 2)
number = int(input("Введите целое число: "))

if number % 3 == 0 and number % 5 == 0:
    print("Число делится на 3 и на 5 одновременно")
else:
    print("Число НЕ делится на 3 и на 5 одновременно")

# 3)
n = int(input("Введите натуральное число n: "))

product = 1

for i in range(1, n + 1):
    product *= i

print("Произведение чисел от 1 до", n, "равно", product)

# 4)
n = int(input("Введите натуральное число n: "))

count = 0

print("Чётные числа от 1 до", n, ":")

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)
        count += 1

print("Количество чётных чисел:", count)