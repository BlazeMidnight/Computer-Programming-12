from random import randint

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

a = MyArrayList()
for i in range(10):
    a.add(randint(1,9))

print(a)
print(a.add(1000))
print(a)
print(a.set(3, 18))
print(a)
    

    
