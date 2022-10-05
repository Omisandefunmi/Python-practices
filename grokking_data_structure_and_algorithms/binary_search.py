def binary_search(list_, item):
    low = 0
    high = len(list_) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list_[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


numbers = [1, 2, 4, 5, 7, 9, 12, 15, 65, 98]
print(binary_search(numbers, 98))

