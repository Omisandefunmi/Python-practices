def cutting_sticks(array):
    result = []
    array.sort()
    min_ = array[0]
    result.append(len(array))
    for i in range(0, len(array)):
        if array[i] > min_:
            min_ = array[i]
            result.append(len(array) - i)
    return result
