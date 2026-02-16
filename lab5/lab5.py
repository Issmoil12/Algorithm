#первое задание

# Проверка корректности n
while True:
    n = int(input("Введите количество элементов n: "))
    if n > 0:
        break
    else:
        print("Ошибка! n должно быть больше 0.")

# Ввод массива
arr = []

for i in range(n):
    num = int(input(f"Введите элемент {i + 1}: "))
    arr.append(num)

print("Полученный массив:", arr)


#второе задание

# Сумма элементов
summa = 0
for i in range(n):
    summa += arr[i]

# Поиск максимума и минимума
max_elem = arr[0]
min_elem = arr[0]

for i in range(n):
    if arr[i] > max_elem:
        max_elem = arr[i]
    if arr[i] < min_elem:
        min_elem = arr[i]

# Среднее арифметическое
average = summa / n

print("Сумма элементов:", summa)
print("Максимальный элемент:", max_elem)
print("Минимальный элемент:", min_elem)
print("Среднее арифметическое:", average)


#третье задание

positive_count = 0
negative_count = 0
even_count = 0

for i in range(n):
    if arr[i] > 0:
        positive_count += 1
    if arr[i] < 0:
        negative_count += 1
    if arr[i] % 2 == 0:
        even_count += 1

print("Количество положительных чисел:", positive_count)
print("Количество отрицательных чисел:", negative_count)
print("Количество чётных чисел:", even_count)


#четвёртое задание

search_num = int(input("Введите число для поиска: "))

found = False

for i in range(n):
    if arr[i] == search_num:
        print("Число найдено. Индекс:", i)
        found = True
        break

if not found:
    print("Число не найдено в массиве.")


#пятое задание

if n < 2:
    print("Невозможно найти второй по величине элемент (массив меньше 2 элементов).")
else:
    first = second = None

    for num in arr:
        if first is None or num > first:
            second = first
            first = num
        elif second is None or (num > second and num != first):
            second = num

    if second is None:
        print("Второго по величине элемента нет (все элементы одинаковые).")
    else:
        print("Второй по величине элемент:", second)