def qsort(array):
    if len(array) < 2:
        return array

    pivot_index = len(array) // 2
    pivot = array[pivot_index]

    left = [x for x in array[:pivot_index] + array[pivot_index+1:] if x <= pivot]
    right = [x for x in array[:pivot_index] + array[pivot_index + 1:] if x > pivot]

    return qsort(left) + [pivot] + qsort(right)

list1 = [4, 2, 8, 0, 1, -5, 9, 7, 6]
list2 = [11, 54, -26, 89, 90, 67, 78, 789, 37, 67]

print(qsort(list1))
print(qsort(list2))