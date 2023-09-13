def bubble(arr):
  n = len(arr)
  for i in range(n):
    print(arr)
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        temp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = temp
    

def binarysearch(value, arr):
  n = len(arr)
  middle = int(n/2)
  
  # Fixed the index error by checking if the list is empty
  if n == 0:
    return None
    
  if (value < arr[middle]):
    return binarysearch(value, arr[:middle]) 
    
  if (value > arr[middle]): 
    return binarysearch(value, arr[middle:]) 
    
  if (value == arr[middle]):
    return middle

# Fixed version of binary search
def binarySearch(value, arr):
    n = len(arr)
    
    if n == 0:  # Base case: array is empty
        return None
    
    middle = n // 2
    
    if value < arr[middle]:
        return binarysearch(value, arr[:middle]) 
    elif value > arr[middle]: 
        result = binarysearch(value, arr[middle+1:])
        return result + middle + 1 if result is not None else None
    else:
        return middle



x = [5,3,4,2,9, 28, 23, 48, 93, -1]


print(binarysearch(-1, x))