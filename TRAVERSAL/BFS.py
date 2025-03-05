class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.__dict__)

    def insert(self,data):
        if self.lookup(data):
            print(f"DATA ALREADY PRESENT --> {data}")
            return
        node = Node(data)
        if not self.root:
            self.root=node
            return
        else:
            temp = self.root
            while True:
                if data < temp.data:
                    if not temp.left:
                        temp.left = node
                        return
                    else:
                        temp = temp.left
                elif data > temp.data:
                    if not temp.right:
                        temp.right=node
                        return
                    else:
                        temp = temp.right

    def lookup(self,data):
        temp = self.root
        while True:
            if not temp: return False
            if data == temp.data:
                return True
            elif  data < temp.data:
                temp = temp.left
            else:
                temp = temp.right

    def remove(self,data):
        temp = self.root
        prev = None
        while True:
            #NULL CHECK
            if not temp: return False

            #LOOKUP ALGO
            if  data < temp.data:
                prev = temp
                temp = temp.left
            elif data > temp.data:
                prev = temp
                temp = temp.right

            #MATCH FOUND!
            elif data == temp.data:
                #NODE HAS NO CHILD
                if not temp.left and not temp.right:
                    if prev.left == temp:
                        prev.left = None
                    else:
                        prev.right = None

                #NODE HAS BOTH CHILD
                elif (temp.left) and (temp.right):
                    successor_ptr = self.successor(temp)
                    item = successor_ptr.data
                    self.remove(item)
                    temp.data = item

                else:
                    if prev.left == temp:
                        if temp.left:
                            prev.left = temp.left
                        else:
                            prev.left = temp.right
                    else:
                        if temp.left:
                            prev.right = temp.left
                        else:
                            prev.right = temp.right

                return

    def successor(self, temp):
        ptr = temp.right
        while(ptr.left):
            ptr = ptr.left
        return ptr

    def breadthFirstSearch(self):
        temp = self.root
        queue=[]
        array=[]
        queue.append(temp)

        while(len(queue)>0):
            temp = queue.pop(0)
            array.append(temp.data)#CURRENT NODE
            if(temp.left):
                queue.append(temp.left)
            if(temp.right):
                queue.append(temp.right)
        print(array)

    def BFS_RECUR(self,queue,array):
        if len(queue) == 0:
            return array
        temp = queue.pop(0)
        array.append(temp.data)
        if (temp.left):
            queue.append(temp.left)
        if (temp.right):
            queue.append(temp.right)

        return self.BFS_RECUR(queue,array)

    def inorder(self,temp):
        if temp:
            self.inorder(temp.left)
            print(f"{temp.data}-->",end='')
            self.inorder(temp.right)

tree = BinarySearchTree()

#INSERT
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)

#TRAVERSAL
tree.inorder(tree.root)
print()

#LOOKUP
#print(f"\n{tree.lookup(15)}")

#REMOVE
# tree.remove(9)

#TRAVERSAL
#INORDER --> tree.inorder(tree.root)
tree.breadthFirstSearch()
#print(tree.BFS_RECUR([tree.root],[]))

