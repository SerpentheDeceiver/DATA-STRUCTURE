class Stack:
    def __init__(self):
        self.arr = []
        self.top = -1

    #to print class variables
    def __str__(self):
        return str(self.__dict__)

    def peek(self):
        return self.arr[self.top]

    def push(self, value):
        self.arr.append(value)
        self.top += 1

    def pop(self):
        popped_item = self.arr[self.top]
        del self.arr[self.top]
        self.top -= 1
        return popped_item

    def show(self):
        print(f"top-->{self.top}",end=" ")
        print(list(self.arr))


mystack = Stack()

mystack.push('google')
mystack.push('microsoft')
mystack.push('facebook')
mystack.push('apple')

mystack.show()
# print(mystack)

x = mystack.peek()
print(f"PEEK ELEMENT--> {x}")

mystack.pop()
mystack.show()

#print(mystack.__dict__)