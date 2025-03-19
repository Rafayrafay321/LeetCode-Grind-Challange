def bubbleSort(list):
    n = len(list)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if list[j] > list[j + 1]:
                list[j],list[j+1] = list[j+1],list[j]
                swapped = True
        if not swapped:
            break
    return list
        

list = [9,8,7,6,5,4]
print(bubbleSort(list))
