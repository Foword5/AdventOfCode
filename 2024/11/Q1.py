import time
from DoublyLinkedList import DoublyLinkedList, Node;

def blinkOnce(list : DoublyLinkedList):
    node = list.head
    while node:
        length = len(str(node.data))
        if node.data == 0:
            node.data = 1
        elif length%2 == 0:
            value1, value2 = str(node.data)[:length//2], str(node.data)[length//2:]
            newNode = Node(int(value2))
            newNode.prev = node
            newNode.next = node.next
            node.data = int(value1)
            node.next = newNode
            node = newNode
        else:
            node.data *= 2024
        node = node.next

def blink(list : DoublyLinkedList, times : int):
    node = list.head
    while node :
        nodeList = [node]
        for i in range(times):
            for nodeElement in nodeList:
                nodeList = nodeBlink(nodeElement)
        node = nodeList[-1].next 
    return list

def nodeBlink(node : Node):
    length = len(str(node.data))
    if node.data == 0:
        # print("case 0")
        node.data = 1
    elif length%2 == 0:
        # print("case even")
        value1, value2 = str(node.data)[:length//2], str(node.data)[length//2:]
        newNode = Node(int(value2))
        newNode.prev = node
        newNode.next = node.next
        node.data = int(value1)
        node.next = newNode
        return [node, newNode]
    else:
        # print("case other")
        node.data *= 2024
    return [node]


if __name__ == "__main__":
    
    list = DoublyLinkedList.build_from_string("965842 9159 3372473 311 0 6 86213 48")
    
    # list = DoublyLinkedList.build_from_string("125 17")
    
    blinks = 25

    start_time = time.time()
        
    blinks = 25
    for i in range(blinks):
        blinkOnce(list)
    
    print(F"took {time.time() - start_time}s")

    print(list.size())