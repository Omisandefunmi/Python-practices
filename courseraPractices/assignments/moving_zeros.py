def moving_zero(lst):
    if len(lst) == 0:
        return []
    zeros = []
    non_zeros = []
    for i in lst:
        if i == 0:
            zeros.append(i)
        else:
            non_zeros.append(i)
    lst = non_zeros + zeros
    return lst


sample = [0, 8, 3, 9, 0, 2, 0, 1, 3]
samp = [0, 0, 0, 0, 0, 0, 0]
sampl = []
print(moving_zero(sampl))
