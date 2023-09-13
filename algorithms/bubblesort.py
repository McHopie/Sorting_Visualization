def bubble(arr):
  n = len(arr)
  for i in range(n):
    print(arr)
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        temp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = temp
    