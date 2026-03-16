# Задача 1
# Класс узла (Node)

class Node:
    def __init__(self, data):
        self.data = data      # данные
        self.next = None      # ссылка на следующий элемент


# Задача 2
# Класс связного списка

class LinkedList:
    def __init__(self):
        self.head = None  # начало списка


    # Задача 3
    # Добавление в начало списка
    def add_to_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    # Задача 4
    # Добавление в конец списка
    def add_to_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node


    # Задача 5
    # Вывод списка
    def print_list(self):
        current = self.head

        while current:
            print(current.data, end=" ")
            current = current.next
        print()


    # Задача 6
    # Поиск элемента
    def search(self, value):
        current = self.head

        while current:
            if current.data == value:
                return True
            current = current.next

        return False


    # Задача 7
    # Удаление первого элемента
    def delete_first(self):
        if self.head:
            self.head = self.head.next


    # Задача 8
    # Подсчёт элементов
    def count(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next

        return count


    # Задача 10
    # Разворот списка
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev



# ============================
# Демонстрация работы
# ============================

linked_list = LinkedList()

# Задача 9
# Ввод 5 чисел
print("Введите 5 чисел:")

for i in range(5):
    num = int(input())
    linked_list.add_to_end(num)

print("Список:")
linked_list.print_list()

# Проверка поиска
value = int(input("Введите число для поиска: "))
print("Найдено:", linked_list.search(value))

# Подсчёт элементов
print("Количество элементов:", linked_list.count())

# Удаление первого элемента
print("Удаляем первый элемент...")
linked_list.delete_first()
linked_list.print_list()

# Разворот списка
print("Разворачиваем список...")
linked_list.reverse()
linked_list.print_list()