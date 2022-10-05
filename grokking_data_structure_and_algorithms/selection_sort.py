def find_smallest_item(list_):
    smallest_index = 0
    for i in range(1, len(list_)):
        if list_[i] < list_[smallest_index]:
            smallest_index = i
    return smallest_index


def selection_sort(list_):
    new_list = []
    for i in range(0, len(list_)):
        smallest = find_smallest_item(list_)
        new_list.append(list_.pop(smallest))
    return new_list


numbers = [3, 7, 9, 2, 3, 6, 1, 86]
print(find_smallest_item(numbers))
print(selection_sort(numbers))


