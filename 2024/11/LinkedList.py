class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    @classmethod
    def from_string(cls, string : str):
        list = LinkedList()
        splited = string.split(" ")
        for element in splited:
            list.append(int(element))
        return list

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def delete(self, data):
        current = self.head
        previous = None
        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return
            previous = current
            current = current.next

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count