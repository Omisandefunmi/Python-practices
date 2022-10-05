import math


def extraLongFactorials(n):
    # print(factorial(n))
    pass


def factorial(num):
    result = 1
    if num == 1:
        return result
    else:
        result = math.factorial(num)
    return result


course = {'1': 'CIT590',
          '2': 'CIT591',
          '3': 'CIT593'}
# print(course.get('1'))

# d = {}
# d[1] = 1
# d['1'] = 2
# d[1] = 3
# sum = 0
# for i in d:
#     sum += d[i]
# print(sum)


# if __name__ == '__main__':
#     n = int(input().strip())
#
#     extraLongFactorials(n)

# print(factorial(5))

d = {'A': 1, 'B': 2, 'C': 3}

del d['A']
print(d)
