class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def peek(self):
        return self.top.data

    def push(self,data):
        node = Node(data)
        if self.top == None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.length+=1

    def pop(self):
        if not self.top:
            return None
        else:
            data = self.top.data
            self.top = self.top.next
            self.length-=1
            if self.length == 0:
                self.top = None
            return data

    def printt(self):
        temp = self.top
        while temp != None:
            print(temp.data, end=' -> ')
            temp = temp.next
        print()

mystack = Stack()

mystack.push('google')
mystack.push('microsoft')
mystack.push('facebook')
mystack.push('apple')

mystack.printt()

x = mystack.peek()
print(x)

y = mystack.pop()
print(y)

mystack.printt()

qw = mystack.peek()
print(qw)
