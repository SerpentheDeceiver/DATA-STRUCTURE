class Array:
    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return str(self.__dict__)

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length += 1

    def pop(self):
        lastitem = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return lastitem

    def delete(self, index):
        if index==self.length-1:
            return self.pop()
        else:
            deleteditem = self.data[index]
            del self.data[index]

            # for i in range(index, self.length - 1):
            #     self.data[i] = self.data[i + 1]
            #
            # del self.data[self.length - 1]

            self.length -= 1
            return deleteditem

    def show(self):
        print(f"Length-->{self.length}",end=" ")
        print(list(self.data.values()))


arr = Array()

arr.push(3)
arr.push('hi')
arr.push(34)
arr.push(20)
arr.push('hey')
arr.push('welcome')

arr.pop()

arr.push("GANESH")
arr.show()

arr.delete(4)
arr.show()
