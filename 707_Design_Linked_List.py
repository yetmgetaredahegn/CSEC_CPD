class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def addAtHead(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def addAtTail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def deleteAtHead(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def deleteAtTail(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return -1
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value

    def getNode(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def addAtIndex(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.addAtHead(value)
            return True
        if index == self.length:
            self.addAtTail(value)
            return True
        new_node = Node(value)
        temp = self.getNode(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.deleteAtHead()
        if index == self.length - 1:
            return self.deleteAtTail()
        prev = self.getNode(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
