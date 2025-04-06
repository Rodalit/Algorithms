def binary_search(array, item):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(list1, 5)) # => 4
print(binary_search(list1, 8)) # => 7
print(binary_search(list1, 32)) # => None