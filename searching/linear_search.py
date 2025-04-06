def linear_search(array, item):
	for i in range(len(array)):
		if array[i] == item:
			return i
	return None

list1 = [3, 9, 8, 2, 1, 4, 6, 5, 7]
print(linear_search(list1, 6))