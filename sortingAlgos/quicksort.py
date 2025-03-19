def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        lesser = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quickSort(lesser) +[pivot] + quickSort(greater)

arr = [8,7,6,5,4,3,23]
print(quickSort(arr))