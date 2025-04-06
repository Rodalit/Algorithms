def find_smallest(array):
    smallest = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index

def selection_sort(array):
    new_array = []
    for i in range(len(array)):
        smallest = find_smallest(array)
        new_array.append(array.pop(smallest))
    return new_array

list1 = [3, 2, 8, 0, 1, 5, 9, 7, 6]
list2 = [12, 54, 26, 89, 90, 67, 78, 49, 37]
list3 = [567, 59, 2, 689, 41, 50, 408, 23, 34]

print(selection_sort(list1))
print(selection_sort(list2))
print(selection_sort(list3))