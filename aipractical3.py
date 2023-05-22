# implement greedy search algorithm for selection sort

def selectionSort(array, size):
    for index in range(size):
        min_index = index

        for j in range(index + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        (array[index], array[min_index]) = (array[min_index], array[index])


arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
size = len(arr)
selectionSort(arr, size)

print('The array after sorting in ascending order by selection sort is: ')

print(arr)