class HashTable:

    def __init__(self,size):
        self.bucket = size
        self.hashmap = [[] for x in range(self.bucket)]
        # self.items = []
        # self.keys=[]
        # self.values=[]

    def __str__(self):
        return str(self.__dict__)

    def hash(self,key):
        return key % self.bucket

    def put(self,key,value):
        hash = self.hash(key)
        bucket = self.hashmap[hash]
        for item in bucket:
            if item[0]==key and item[1]==value:
                return
        # self.items.append([key,value])
        # self.keys.append(key)
        # self.values.append(value)
        self.hashmap[hash].append([key, value])

    def get(self,key):
        hash = self.hash(key)
        bucket = self.hashmap[hash]
        for item in bucket:
            if item[0] == key:
                return item[1]
        return -1

    def remove(self,key):
        hash = self.hash(key)
        bucket = self.hashmap[hash]
        for item in bucket:
            if item[0] == key:
                bucket.remove(item)
                return
        print("ELEMENT NOT FOUND!!")

h = HashTable(10)
h.put(101,"GANESH")
h.put(101,"ARUMUGAM")
h.put(277,"DEEPAK")
h.put(899,"AISWIN")

print(h)
print(f"VALUE AT 277 hash({h.hash(277)}) --> {h.get(277)}")
print(f"INBUILT HASH FUNCTION IN PYTHON --> {hash("ganesh")},{hash(190)}")
h.remove(899)
print(h)