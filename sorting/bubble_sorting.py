def bubble_sort(array):
    n = len(array)

    for j in range(n - 1):
        for i in range(n - 1 - j):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

    return array

list1 = [2, 5, 1, 3, 4, 6, 9, 8, 7, 0]
print(bubble_sort(list1))