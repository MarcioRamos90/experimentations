
def bubbleSort(arr):
    for i in range(len(arr)):
        for _j in range(0, len(arr) - i -1):
            breakpoint()
            if arr[_j] > arr[_j+1]:
                temp = arr[_j]
                arr[_j] = arr[_j+1]
                arr[_j+1] = temp
    return arr


data = [-2, 45, 0, 11, -9]

print(bubbleSort(data))