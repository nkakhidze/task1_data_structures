# Задание 9: Деревья
# Создайте:
# 1. Бинарное дерево поиска
# 2. Методы добавления и поиска элементов
# 3. Обход дерева в разных порядках (in-order, pre-order, post-order)






class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class binar_tree:
    def __init__(self, root = None):
        self.root = root

    def add_node(self, new_node):
        if self.root is None:
            self.root = new_node
            return f"Назначен root дерева. Значение {self.root.value}, левый сосед: {self.root.left}, правый сосед: {self.root.right}."

        current_node = self.root

        while True:
            if new_node.value == current_node.value:
                return f"В дереве уже есть узел со значением {new_node.value}."

            elif new_node.value < current_node.value:
                if current_node.left is None:
                    current_node.left = new_node
                    return f"Узел {new_node.value} добавлен слева от узла {current_node.value}."
                else:
                    current_node = current_node.left

            else:
                if current_node.right is None:
                    current_node.right = new_node
                    return f"Узел {new_node.value} добавлен справа от узла {current_node.value}."
                else:
                    current_node = current_node.right

    def bypass_in_order(self):
        """лево → текущий узел → право"""
        listik = []
        current_node = self.root

        def go_around(node):
            if node is None:
                return
            if node.left: #Оказывается, лишний
                go_around(node.left)
            listik.append(node.value)
            if node.right:    #Оказывается, лишний
                go_around(node.right)

        go_around(current_node) # открываем стек вызовов

        return listik



    def bypass_pre_order(self):
        """Сначала посещаем сам узел, потом его детей"""
        listik = []
        current_node = self.root

        def go_around(node):
            if node is None:
                return
            listik.append(node.value)

            if node.left:
                go_around(node.left)
            if node.right:
                go_around(node.right)

        go_around(current_node) # открываем стек вызовов

        return listik

    def bypass_post_order(self):
        """Текущий узел обрабатывается последним."""
        listik = []
        current_node = self.root

        def go_around(node):
            if node is None:
                return
            if node.left:
                go_around(node.left)
            if node.right:
                go_around(node.right)
            listik.append(node.value)

        go_around(current_node)  # открываем стек вызовов

        return listik

    def find_node(self, method=bypass_in_order):
        pass




# a1 = Node(1)
# a3 = Node(3)
# a4 = Node(4)
# a5 = Node(5)
# a7 = Node(7)
# a10 = Node(10)
# a20 = Node(20)
# a15 = Node(15)
# # a8 = Node(8)
# # a5 = Node(5)
# # a3 = Node(3)
# # a8 = Node(8)
#
# a5.left = a3
# a5.right = a7
# a10.left = a5
# a10.right = a20
# a20.left = a15
# tree = binar_tree(a10)
# print(tree.bypass_post_order())



tree = binar_tree()

for value in [50, 30, 70, 20, 40, 60, 80, 10, 25, 45, 55, 65, 90]:
    tree.add_node(Node(value))

# print(tree.bypass_in_order()) #== [10, 20, 25, 30, 40, 45, 50, 55, 60, 65, 70, 80, 90]
assert tree.bypass_in_order() == [10, 20, 25, 30, 40, 45, 50, 55, 60, 65, 70, 80, 90]
assert tree.bypass_pre_order() == [50, 30, 20, 10, 25, 40, 45, 70, 60, 55, 65, 80, 90]
assert tree.bypass_post_order() == [10, 25, 20, 45, 40, 30, 55, 65, 60, 90, 80, 70, 50]

# assert tree.find_element(50) is not None
# assert tree.find_element(10) is not None
# assert tree.find_element(90) is not None
# assert tree.find_element(999) is None

print("Все проверки прошли успешно")