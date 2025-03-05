class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def peek(self):
        return self.front.data

    def enqueue(self,data):
        node = Node(data)
        if self.length == 0:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.length+=1

    def dequeue(self):
        if self.length == 0:
            return None
        else:
            dequeue_element = self.front.data
            self.front = self.front.next
            self.length -= 1
            return dequeue_element

    def printt(self):
        temp = self.front
        while temp != None:
          print(temp.data , end = '->')
          temp = temp.next
        print()
        print(self.length)

myq = Queue()

myq.enqueue('google')
myq.enqueue('microsoft')
myq.enqueue('facebook')
myq.enqueue('apple')

myq.printt()

myq.dequeue()
myq.printt()

x = myq.peek()
print(x)