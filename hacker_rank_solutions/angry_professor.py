import doctest


def is_class_cancelled(lst, num):
    """
    //Function to check numbers less than zero or equal to zero, in a list
    :param lst: list
    :param num: int
    :return : str

    >>> is_class_cancelled([0, -1, 2, -4], 3)
    'Yes'
    >>> is_class_cancelled([0, 5, 9, -2], 3)
    'No'
    """

    filter_obj = list(filter(lambda x: x <= 0, lst))
    if len(filter_obj) >= num:
        return 'Yes'
    return 'No'


if __name__ == "__main__":
    print(doctest.testmod())
