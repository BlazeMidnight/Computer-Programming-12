import statistics
arr = [3, 2, 5, 7, 1, 4, 6, 9, 8]

def insertionSort(arr): 
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    return arr

## Runtime = O(n^2)
## Space Complexity = O(n) 
## What data structure will reduce runtime to nlogn? 
##   Linked lists will reduce the runtime to nLogn. This is because 
##   with linked lists inseted of the for loop at the begining of
##   the algorithm. Insted we can use a varible to get the next node's
##   data if the current node is not the tail (for linked list & 
##   double linked list) or if a varible that count up based on 
##   what node you are on is equal to the size of the list (Circularly 
##   Doubly Linked List). 

def selectionSort(arr):
    size = len(arr)
    for s in range(len(arr)):
        minIdx = s
        for i in range(s+1, len(arr)):
            if arr[i] < arr[minIdx]:
                minIdx = i
        (arr[s], arr[minIdx]) = (arr[minIdx], arr[s])
    return arr
## Runtime = O(n^2)
## Space Complexity = O(n) 
    
def quickSort(arr):
    return quickSortH(arr, 0, len(arr)-1)

def quickSortH(arr, low, high):
    if low < high:
        pivot = low - 1
        for i in range(low, high):
            if arr[i] <= arr[high]:
                pivot += 1
                (arr[pivot], arr[i]) = (arr[i], arr[pivot])
        (arr[pivot + 1], arr[high]) = (arr[high], arr[pivot + 1])
        pi = pivot + 1

        quickSortH(arr, low, pi - 1)
        quickSortH(arr, pi + 1, high)
    return arr
    
## Runtime = O(nlogn)
## Space Complexity = O(n) 
## Does your algorithm ever fall into worse case scenario >>> becoming insertion sort? 
##   Yes, it can fall into the wrost case depending on the numbers in the list. This is 
##   because the quickSort's pivot starts at 1, which usally isn't the quickest way to
##   sort. 
## Is it in place? And how does that choice effect space Complexity? 
##   Yes, the list is in place and it is not sorted into another list. Making a new list 
##   adds to the space complexity, while keeping the original list for takes up the least
##   space.

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right) 
        CurrlenLeft = 0
        CurrlenRight = 0
        lenArr = 0

        while CurrlenLeft < len(left) and CurrlenRight < len(right):
            if left[CurrlenLeft] < right[CurrlenRight]:
                arr[lenArr] = left[CurrlenLeft]
                CurrlenLeft += 1
            else:
                arr[lenArr] = right[CurrlenRight]
                CurrlenRight += 1
            lenArr += 1

        while CurrlenLeft < len(left):
            arr[lenArr] = left[CurrlenLeft]
            CurrlenLeft += 1
            lenArr += 1

        while CurrlenRight < len(right):
            arr[lenArr] = right[CurrlenRight]
            CurrlenRight += 1
            lenArr += 1
    return arr

## Runtime = O(nlogn)
## Space Complexity = O(n) 

arr = [0,1,3,5,7,9,2,4,6,8] 
print(insertionSort(arr))
print(selectionSort(arr))
print(quickSort(arr)) 
print(mergeSort(arr)) 
    
    
    
