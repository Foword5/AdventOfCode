class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    @classmethod
    def build_from_string(cls, string : str):
        list = DoublyLinkedList()
        splited = string.split(" ")
        for element in splited:
            list.append(int(element))
        return list

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def delete(self, node):
        if self.head is None or node is None:
            return
        if self.head == node:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next

    def __str__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next
        return " ".join(map(str, nodes))
        
    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
