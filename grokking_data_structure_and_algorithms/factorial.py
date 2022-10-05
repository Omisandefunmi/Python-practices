def find_factorial_of_(number):
    if number == 1:
        return 1
    else:
        return number * find_factorial_of_(number - 1)


print(find_factorial_of_(4))
