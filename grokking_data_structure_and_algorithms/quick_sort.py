def quick_sort(list_):
    if len(list_) < 2:
        return list_
    pivot = list_[0]
    lesser = [i for i in list_[1:] if i <= pivot]
    greater = [i for i in list_[1:] if i > pivot]
    return quick_sort(lesser) + [pivot] + quick_sort(greater)


print(quick_sort([4, 7, 9, 3, 0, 1, 7, 4]))
