import random

# =========================
# ЗАДАНИЕ 1 + 2
# =========================

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matrix = []

# Заполнение матрицы случайными числами от 1 до 20
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

# Сумма всех элементов и максимальный элемент
total = 0
maximum = matrix[0][0]

for row in matrix:
    for value in row:
        total += value
        if value > maximum:
            maximum = value

print("\nСумма всех элементов:", total)
print("Максимальный элемент:", maximum)

# =========================
# ЗАДАНИЕ 2 (дополнение)
# =========================

# Сумма по строкам
row_sums = []

print("\nСуммы по строкам:")
for i in range(rows):
    row_sum = sum(matrix[i])
    row_sums.append(row_sum)
    print(f"Сумма строки {i}: {row_sum}")

# Сумма по столбцам
print("\nСуммы по столбцам:")
for j in range(cols):
    col_sum = 0
    for i in range(rows):
        col_sum += matrix[i][j]
    print(f"Сумма столбца {j}: {col_sum}")

# Строка с максимальной суммой
max_row_index = row_sums.index(max(row_sums))
print("\nСтрока с максимальной суммой:", max_row_index)

# =========================
# ЗАДАНИЕ 3 (мини-проект 4x4)
# =========================

def shift_right(row):
    new_row = [x for x in row if x != 0]
    zeros = [0] * (len(row) - len(new_row))
    return zeros + new_row

# Создание поля 4x4 с числами от 0 до 9
matrix_4x4 = []

for i in range(4):
    row = []
    for j in range(4):
        row.append(random.randint(0, 9))
    matrix_4x4.append(row)

print("\nПоле 4x4 ДО сдвига:")
for row in matrix_4x4:
    print(row)

# Сдвиг вправо
for i in range(4):
    matrix_4x4[i] = shift_right(matrix_4x4[i])

print("\nПоле 4x4 ПОСЛЕ сдвига вправо:")
for row in matrix_4x4:
    print(row)