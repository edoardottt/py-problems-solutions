def insertionSortRecursive(arr, n):
    if n <= 1:
        return
    insertionSortRecursive(arr, n - 1)
    last = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j = j - 1

    arr[j + 1] = last


def printArray(arr, n):
    for i in range(n):
        print(arr[i])
