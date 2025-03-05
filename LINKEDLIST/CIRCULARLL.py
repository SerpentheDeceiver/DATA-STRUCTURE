class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CIRCULARLL:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        node = Node(data)
        if self.length == 0:
            node.next = node
            self.head = self.tail = node
        else:
            node.next = self.head
            self.tail.next = node
            self.tail = self.tail.next
        self.length += 1

    def prepend(self, data):
        node = Node(data)
        if self.length == 0:
            node.next = node
            self.head = self.tail = node
        else:
            node.next = self.head
            self.tail.next = node
            self.head = node
        self.length += 1

    def insert(self, index, data):
        node = Node(data)
        if (index == 0):
            self.prepend(data)
        elif (index  == self.length+1):
            self.append(data)
        else:
            temp = self.head
            for i in range(1, index):
                temp = temp.next
            node.next = temp.next
            temp.next = node

    def remove(self, index):

        if (index) > (self.length):
            print("INVALID INDEX!!!")
            return

        if (index == 0):
            self.head = self.head.next
            self.tail.next = self.head
        else:
            temp = self.head
            for i in range(1, index):
                temp = temp.next
            temp.next = temp.next.next
        self.length -= 1

    def printl(self):
        temp = self.head
        print('Length = ' + str(self.length), end=" :) ")
        for i in range(self.length+1):
            print(f"{temp.data}->",end='')
            temp = temp.next
        print()

l = CIRCULARLL()
# append
l.append(10)
l.append(5)
l.append(6)
# prepend
l.prepend(1)
# insert
l.insert(2, 99)
l.insert(5,100)
# l.insert(34, 23)
# printl
l.printl()
# remove
l.remove(4)
# printl
l.printl()

