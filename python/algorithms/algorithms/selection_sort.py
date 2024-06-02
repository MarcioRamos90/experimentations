def selectionSort(array, size):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if array[min_idx] > array[i]:
                min_idx = i
        array[step], array[min_idx] = array[min_idx], array[step]


data = [12, -2, 45, 0, 11, -9, -10]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)