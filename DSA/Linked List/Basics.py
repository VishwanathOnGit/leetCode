class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        current = self.head
        while current != None:
            print(current.value)
            current = current.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    

my_linked_list = LinkedList(5)
my_linked_list.append(6)
my_linked_list.append(11)
my_linked_list.print_list()