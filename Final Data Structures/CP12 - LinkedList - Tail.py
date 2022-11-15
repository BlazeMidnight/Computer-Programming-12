from math import log10

class Node:
    __data = None
    __nxt = None
    def __init__(self, data, nxt=None):
        self.__data = data
        self.__nxt = nxt

    def __str__(self):
        d = self.__data
        n = self.__nxt

        return "Data: "+str(d)+" >> "+str(type(n))

    def hasNext(self):
        return self.__nxt != None

    def getNext(self):
        return self.__nxt
    def setNext(self, nxt):
        self.__nxt = nxt

    def getData(self):
        return self.__data
    def setData(self, data):
        self.__data = data

class myLinkedList:
    __head = None
    __tail = None
    __size = 0

    def __init__(self):
        self.__head = None
        

    def __str__(self):
        curr = self.__head
        out = "<0> ... "
        if(curr != None):
            out += str(curr)

        i = 1
        while(curr.hasNext()):
            curr = curr.getNext()
            out += "\n<"+str(i)+"> "+("..."[int(log10(i)):])+" "+str(curr)
        return out

    def add(self, element):
        newNode = Node(element)
        if self.__head == None:
            self.__head = newNode
        else:
            self.__tail.setNext(newNode)
        self.__tail = newNode
        self.__size += 1
        return
 
    def remove(self, index):
        if index > self.__size:
            return
        if index == 1 or index == self.__size:
            self.__head = self.__head.getNext
        if index == self.__size:
            self.__tail = 1
        
        curr = self.__head
        prev = None
        for i in range(1, self.__size+1):
            if(i == index):
                prev.setNext(curr.getNext())
                self.__size -= 1
                return
            else:
                prev = curr
                curr = curr.getNext()
        

    def get(self, index):
        curr = self.__head
        while curr.getData() is not index:
            if curr == None:
                return None
            curr = curr.getNext()
        return curr.getData()

    def set(self, element, index):
        if index > self.__size:
            return
        curr = self.__head
        for i in range(1, index):
            curr = curr.getNext()
        curr.setData(element)
        return

    def isEmpty(self):
        return self.__head == None 

    def size(self):
        return self.__size

LL = myLinkedList()
LL.add(3)
LL.add(4)
LL.add(5)
LL.add(6)

LL.remove(6)

LL.add(9)



print(LL)



    

