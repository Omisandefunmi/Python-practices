def last_but_one(seq):
    if len(seq) == 0:
        return None
    lst = []
    for item in range(0, len(seq) - 1):
        lst.append(seq[item])
    return lst


okay = [2, 3, 6, 5, 8]
print(last_but_one(okay))

