def min_and_max(lst):
    return max(lst), min(lst)


def main():
    lists = [23, 4, 12, 86, 98, -67, 40]
    print(min_and_max(lists))
    print(type(min_and_max(lists)))


if __name__ == '__main__':
    main()
