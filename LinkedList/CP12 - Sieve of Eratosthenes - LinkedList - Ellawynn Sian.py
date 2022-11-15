from math import log10
import math
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
        if not self.__head:
            self.__head = newNode
        elif self.__tail:
            self.__tail.setNext(newNode)
            self.__tail = newNode
        else:
            self.__head.setNext(newNode)
            self.__tail = newNode
        self.__size += 1
        return
 
    def remove(self, index):
        if index > self.__size:
            return
        if index == 0:
            self.__head = self.__head.getNext()
            return
        curr = self.__head
        prev = None
        for i in range(self.__size):
            if(i == index):
                prev.setNext(curr.getNext())
                if self.__size-1 == index:
                    self.__tail = prev
                self.__size -= 1
                return
            else:
                prev = curr
                curr = curr.getNext()
        

    def get(self, index):
        curr = self.__head
        for i in range(index):
            curr = curr.getNext()
        if curr == None:
            return None
        else:
            return curr.getData()

    def set(self, element, index):
        newNode = Node(element)
        if index >= self.__size:
            return
        if index == 0:
            self.__head = self.__head.getNext()
            newNode.setNext(self.__head)
            self.__head = newNode
            return 
        curr = self.__head
        for i in range(index):
            curr = curr.getNext()
        curr.setData(element)
        return

    def isEmpty(self):
        return self.__head == None 

    def size(self):
        return self.__size

def sieveOfEratosthenes(n):
    primes = myLinkedList()
    index = 2
    addNum = 1
    for i in range(1, n):
        primes.add(addNum + i)

    while(i <= math.sqrt(n)):
        for j in range(i*2, number+1, i):
            if j in primes:
                primes.remove(j)

    index = index + 1
    return primes




def iterativeSieve(n):
    primesList = myLinkedList()
    num = 2
    for i in range(n):
        flag = True
        for i in range(primesList.size()):
            prime = primesList.get(i)
            if num % prime == 1:
                flag = False
                break


        if flag == True:
            primesList.add(num)

        num += 1

    return primesList
        
        



print(sieveOfEratosthenes(10))


    
