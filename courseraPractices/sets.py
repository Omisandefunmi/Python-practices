a = 'abradabra'

set_a = set(a)
print(set_a)

b = [9, 6, 3, 5, 3, 9, 2, 10, 10]
print(type(b))
b_set = set(b)

print(b_set)

#How to declare a set
empty_set = set()
print(empty_set)

#iterating through a list
for number in b_set:
    print(number, end=', ')

