def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        smallestInd = i
        for j in range(i + 1,n):
            if arr[j] < arr[smallestInd]:
                smallestInd = j
        arr[i],arr[smallestInd] = arr[smallestInd],arr[i]
    return arr

arr = [7,5,4,3,2]
print(selectionSort(arr))