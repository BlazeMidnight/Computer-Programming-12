from random import randint
import math

class MyArrayList:
    arr = []
    __size = 0

    def __init__(self):
        self.arr = [None]*10

    def __str__(self): ##overriding
        return "["+", ".join([str(a) for a in self.arr])+"]"

    def get(self, index): ##index out of bound error thrown in the future
        if(self.arr[index] != None):
            return self.arr[index]
        else:
            raise IndexError("Please make sure you index input is correct.")

    def set(self, element, index): ## index out of bounds error thrown in the future
        if(self.arr[index] != None):
            self.arr[index] = element
        else:
            raise IndexError("Please make sure you index input is correct.")

    def size(self):
        return self.__size

    def isEmpty(self):
        return a.size() == 0


    def add(self, element): 
        if(self.__size >= len(self.arr)):
            newArr = [None]*len(self.arr)*2
            for i in range(0, len(self.arr)):
                newArr[i] = self.arr [i]
            self.arr = newArr
        self.arr[self.__size] = element
        self.__size += 1
        return


    def remove(self, index): ##remove via index
        for i in range(index,len(self.arr)-1):
            self.arr[i] = self.arr[i+1]
            if(self.arr[i] == None):
                break


def sieveOfEratosthenes(n):
    primes = MyArrayList()
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
    primesList = MyArrayList()
    n = 2
    while(primesList.size() < n):
        flag = True
        for i in range(primesList.size()):
            prime = primesList.get(i)
            if n%i == 0:
                flag = false
        if flag:
            primesList.add(n)
        n+= 1
    return primesList



    '''
    for i in range(n):
        flag = True
        while flag:
            for i in range(primesList.size()):
                prime = primesList.get(i)
                if num % prime == 1:
                    flag = False
                    break
                if prime*prime > num:
                    break
        if flag == True:
            primesList.add(num)
            num += 1
    return primesList
    '''
        






print(iterativeSieve(1000))
        
    

    

    
