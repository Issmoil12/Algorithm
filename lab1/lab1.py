# 1)
a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))

sum_numbers = a + b
difference = a - b
product = a * b

print("Сумма:", sum_numbers)
print("Разность:", difference)
print("Произведение:", product)

# 2)
number = int(input("Введите целое число: "))

if number > 0:
    print("Число положительное")
elif number < 0:
    print("Число отрицательное")
else:
    print("Число равно нулю")

# 3)

n = int(input("Введите натуральное число n: "))

sum_numbers = 0

for i in range(1, n + 1):
    sum_numbers += i

print("Сумма чисел от 1 до", n, "равна", sum_numbers)

