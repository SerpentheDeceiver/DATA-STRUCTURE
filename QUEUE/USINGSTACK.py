class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.length = len(self.stack2)

    def __str__(self):
        return str(self.__dict__)

    def enqueue(self, x: int) -> None:
        self.stack1.append(x)

    def dequeue(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        #EMPTY CASE
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self,stack) -> bool:
        if not stack:
            return True
        return False

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()

obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)

print(obj)

param_2 = obj.dequeue()
print(f"DEQUEUE ELEMENT: {param_2}")

print(obj)

param_3 = obj.peek()
print(f"PEEK ELEMENT: {param_3}")

