def linear_search(arr,item):
    for i in range(len(arr)):
        if(arr[i] == item):
            return i
    return -1
pos1 = linear_search([30,20,10,2,30,90,10],30)
