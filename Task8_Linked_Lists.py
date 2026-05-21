

class Node():
    def __init__(self, value=None, next = None):
        self.value = value
        self.next = next


class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def add_element(self, value):
        pass

    def delete_element(self):
        pass

    def find_element(self):
        pass

    def show_linked_list(self):
        pass


# 1. Создать новый Node со значением value.
# 2. Если список пустой:
#        self.head = новый узел
# 3. Если список не пустой:
#        идти от self.head до последнего узла
#        у последнего узла next сделать новым узлом