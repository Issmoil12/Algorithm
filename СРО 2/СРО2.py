# =========================
# Узел дерева
# =========================
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# =========================
# Бинарное дерево
# =========================
class BinaryTree:
    def __init__(self):
        self.root = None

    # Добавление узла (как в бинарном дереве поиска)
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)


# =========================
# Визуализация дерева (боком)
# =========================
    def print_tree(self):
        self._print_tree(self.root, 0)

    def _print_tree(self, node, level):
        if node is not None:
            self._print_tree(node.right, level + 1)
            print("    " * level + str(node.value))
            self._print_tree(node.left, level + 1)


# =========================
# Вывод по уровням
# =========================
    def print_levels(self):
        if not self.root:
            return

        queue = [self.root]

        while queue:
            next_level = []
            for node in queue:
                print(node.value, end=" ")
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            print()
            queue = next_level


# =========================
# ТЕСТ
# =========================
def main():
    tree = BinaryTree()

    values = [50, 30, 70, 20, 40, 60, 80]
    for v in values:
        tree.insert(v)

    print("=== Иерархия дерева (визуализация) ===")
    tree.print_tree()

    print("\n=== Вывод по уровням ===")
    tree.print_levels()


main()