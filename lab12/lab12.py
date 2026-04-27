# =========================
# Задание 1
# =========================
def task1():
    students = {
        "Ali": 85,
        "Dana": 90,
        "Arman": 78,
        "Mira": 92
    }

    print("\n1) Студенты и оценки:")
    for name, grade in students.items():
        print(name, "-", grade)


# =========================
# Задание 2
# =========================
def task2():
    arr = [5, 2, 5, 3, 2, 5]
    freq = {}

    for x in arr:
        freq[x] = freq.get(x, 0) + 1

    print("\n2) Частота чисел:", freq)


# =========================
# Задание 3
# =========================
def task3():
    text = "algorithm"
    freq = {}

    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1

    print("\n3) Частота символов:", freq)


# =========================
# Задание 4
# =========================
def task4():
    phonebook = {
        "Ali": "87001112233",
        "Dana": "87002223344",
        "Arman": "87003334455",
        "Mira": "87004445566",
        "Dias": "87005556677"
    }

    name = "Arman"
    print("\n4) Телефон Армана:", phonebook.get(name, "Не найден"))


# =========================
# Задание 5
# =========================
def task5():
    words = ["cat", "dog", "cat", "bird", "dog", "dog"]
    freq = {}

    for w in words:
        freq[w] = freq.get(w, 0) + 1

    print("\n5) Повторяющиеся слова:")
    for k, v in freq.items():
        if v > 1:
            print(k)


# =========================
# Задание 6
# =========================
def task6(a, b):
    print("\n6) Анаграммы:")

    return sorted(a) == sorted(b)


# =========================
# Задание 7
# =========================
def task7():
    products = {
        "apple": 500,
        "banana": 300
    }

    # добавление
    products["orange"] = 400

    # изменение
    products["apple"] = 550

    # удаление
    del products["banana"]

    # поиск
    print("\n7) Цена apple:", products.get("apple"))

    print("Все товары:", products)


# =========================
# Задание 8
# =========================
def task8():
    arr = [4, 7, 1, 9, 7, 3, 1]
    seen = set()

    print("\n8) Первое повторение:")

    for x in arr:
        if x in seen:
            print(x)
            return
        seen.add(x)


# =========================
# Задание 9
# =========================
def task9():
    text = "python is great and python is easy"
    words = text.lower().split()

    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1

    most = max(freq, key=freq.get)

    print("\n9) Самое частое слово:", most)


# =========================
# Задание 10 (хеш-таблица)
# =========================
class HashTable:
    def __init__(self, size=5):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash(key)
        self.table[index].append(key)

    def display(self):
        print("\n10) Хеш-таблица:")
        for i, bucket in enumerate(self.table):
            print(i, ":", bucket)


# =========================
# RUN ALL
# =========================
def main():
    task1()
    task2()
    task3()
    task4()
    task7()
    task8()
    task9()

    print("\n6)", task6("listen", "silent"))

    ht = HashTable()
    for x in [1, 6, 11, 16, 21]:
        ht.insert(x)
    ht.display()

    task5()

main()