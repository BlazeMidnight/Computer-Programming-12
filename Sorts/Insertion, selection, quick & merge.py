arr = [3, 2, 5, 7, 1, 4, 6, 9, 8]

def insertionSort(arr): 
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

def selectionSort(arr):
    size = len(arr)
    for s in range(len(arr)):
        minIdx = s
        for i in range(s+1, len(arr)):
            if arr[i] < arr[minIdx]:
                minIdx = i
        (arr[s], arr[minIdx]) = (arr[minIdx], arr[s])
        
    
def quickSort(arr):
    return quickSortH(arr, 0, len(arr)-1)

def quickSortH(arr, low, high):
    if low < high:
        i = low - 1
        for j in range(low, high):
            if arr[j] <= arr[high]:
                i += 1
                (arr[i], arr[j]) = (arr[j], arr[i])
        (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
        pi = i + 1

        quickSortH(arr, low, pi - 1)
        quickSortH(arr, pi + 1, high))

def mergeSort(arr):
  if len(arr) <= 1:
    return arr
  mid = len(arr) // 2
  l = mergeSort(arr[:mid])
  r = mergeSort(arr[mid:])
  return mergeSortH(l, r)

def mergeSortH(left, right):
  result = []
  while (left and right):
    if left[0] < right[0]:
      result.append(left[0])
      left.pop(0)
    else:
      result.append(right[0])
      right.pop(0)

  if left:
    result += left
  if right:
    result += right
  return result
            
arr = [0,1,3,5,7,9,2,4,6,8] 
print(mergeSort(arr)) 
            
arr = [0,1,3,5,7,9,2,4,6,8] 
print(mergeSort(arr)) 

quickSort(arr)
print(arr)
