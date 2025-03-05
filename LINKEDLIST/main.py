class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self,data):
        node = Node(data)
        if self.length == 0:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
        self.length+=1

    def prepend(self,data):
        node = Node(data)
        if self.length == 0:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length+=1

    def insert(self,index,data):
        node = Node(data)
        if(index == 0):
            self.prepend(data)
        elif(index == self.length+1):
            self.append(data)
        else:
            temp = self.head
            for i in range(1,index):
                temp = temp.next
            node.next = temp.next
            temp.next = node

    def remove(self,index):

        if(index)>(self.length):
            print("INVALID INDEX!!!")
            return

        if(index == 0):
            self.head = self.head.next
        else:
            temp = self.head
            for i in range(1,index):
                temp = temp.next
            temp.next = temp.next.next
        self.length-=1

    def printl(self):
        temp = self.head
        print('Length = ' + str(self.length),end=" :) ")
        while temp != None:
            print(f"{temp.data}->", end='')
            temp = temp.next
        print()
    # def reverse(self):
    #     prev = None
    #     self.tail = self.head
    #     while (self.head!=None):
    #         temp = self.head
    #         self.head = self.head.next
    #         temp.next = prev
    #         prev = temp
    #     self.head = prev
    
    def reverse(self):
        prev = None
        temp = self.head
        while self.head:
            self.head = self.head.next
            temp.next = prev
            prev = temp
            temp = self.head
        self.head = prev


l = LinkedList()
#append
l.append(10)
l.append(5)
l.append(6)
#prepend
l.prepend(1)
#insert
l.insert(2, 99)
# l.insert(34, 23)
#printl
l.printl()
#remove
l.remove(3)
#printl
l.printl()
#reverse
l.reverse()
l.printl()