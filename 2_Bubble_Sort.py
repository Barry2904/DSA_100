def bubble():
    arr = [30,20,10,2,30,90,10]
    temp = 0
    for i in range(len(arr)):
        for j in range(len(arr) - i-1):
            if(arr[j] > arr[j+1]):
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
    return arr
  
arr_ = bubble()
print(arr_)


