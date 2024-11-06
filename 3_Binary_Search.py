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

def binary_search(arr,item):
    left,right = 0, len(arr)-1
    for _ in range(len(arr)):
        if(left>right):
            break
        mid = (left + right)//2
        if(arr[mid] == item):
            return mid
        elif arr[mid] > item:
            right = mid - 1
        else:
            left = mid + 1
    return -1


arr_ = bubble()
pos2 = binary_search(arr_,30)

print(arr_)
print(pos2)

