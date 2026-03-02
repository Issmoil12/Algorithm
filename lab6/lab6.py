import random

# Ввод размеров
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

# Создание матрицы
matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(random.randint(1, 20))
    matrix.append(row)

# Вывод матрицы
print("\nМатрица:")
for row in matrix:
    for value in row:
        print(f"{value:4}", end="")
    print()

# Поиск суммы и максимума
total = 0
maximum = matrix[0][0]

for row in matrix:
    for value in row:
        total += value
        if value > maximum:
            maximum = value

print("\nСумма всех элементов:", total)
print("Максимальный элемент:", maximum)

# Сумма по строкам
print("\nСумма по строкам:")
row_sums = []

for i in range(rows):
    row_sum = sum(matrix[i])
    row_sums.append(row_sum)
    print(f"Сумма строки {i}: {row_sum}")

# Сумма по столбцам
print("\nСумма по столбцам:")
for j in range(cols):
    col_sum = 0
    for i in range(rows):
        col_sum += matrix[i][j]
    print(f"Сумма столбца {j}: {col_sum}")

# Строка с максимальной суммой
max_row_index = row_sums.index(max(row_sums))
print("\nСтрока с максимальной суммой:", max_row_index)

import random

# Функция сдвига строки вправо
def shift_right(row):
    new_row = [x for x in row if x != 0]
    zeros = [0] * (len(row) - len(new_row))
    return zeros + new_row

# Создание поля 4x4
matrix = []

for i in range(4):
    row = []
    for j in range(4):
        row.append(random.randint(0, 9))  # числа от 0 до 9
    matrix.append(row)

# Вывод до сдвига
print("До сдвига:")
for row in matrix:
    print(row)

# Сдвиг всех строк вправо
for i in range(4):
    matrix[i] = shift_right(matrix[i])

# Вывод после сдвига
print("\nПосле сдвига вправо:")
for row in matrix:
    print(row)
