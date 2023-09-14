def merge(arr, left, middle, right): 
  n1 = middle - left + 1
  n2 = right - middle 

  L = [0] * n1
  R = [0] * n2

  for i in range(n1): 
    L[i] = arr[i + left]

  for i in range(n2): 
    R[i] = arr[i + middle + 1]

  i = 0
  j = 0 
  k = left

  while i < n1 and j < n2: 
    if L[i] <= R[j]: 
      arr[k] = L[i]


def mergesort(arr, left, right):
  if left < right: 
    middle = (left + right + 1) // 2
    mergesort(arr, left, middle)
    mergesort(arr, middle, right)
    merge(arr, left, middle, right)