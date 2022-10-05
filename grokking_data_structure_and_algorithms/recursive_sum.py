def sum_of_array(list_):
    if list_ == []:
        return 0
    return list_[0] + sum_of_array(list_[1:])


def count_item(list_):
    if list_ == []:
        return 0
    return 1 + count_item(list_[1:])


def find_maximum(list_):
    if len(list_) == 2:
        return max(list_[0], list_[1])


arr = [4, 5, 8, 3]
print(sum_of_array(arr))
print(count_item(arr))
