# 1)
number = int(input("Введите целое число: "))

if number > 0:
    print("Число является положительным")

# 2)
number = int(input("Введите целое число: "))

if number % 2 == 0:
    print("Число чётное")
else:
    print("Число нечётное")\

# 3)
score = int(input("Введите число от 1 до 100: "))

if score < 1 or score > 100:
    print("Ошибка: число вне допустимого диапазона")
elif score >= 90:
    print("Оценка: A")
elif score >= 75:
    print("Оценка: B")
elif score >= 60:
    print("Оценка: C")
else:
    print("Оценка: D")

# 4)
age = int(input("Введите возраст: "))
student = input("Есть ли студенческий билет? (да/нет): ")

if age < 18 or student == "да":
    print("Вы имеете право на льготный тариф")
else:
    print("Льготный тариф не предоставляется"

# 5)
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

if a > b:
    print("Первое число больше второго")
else:
    if a < b:
        print("Второе число больше первого")
    else:
        print("Числа равны")