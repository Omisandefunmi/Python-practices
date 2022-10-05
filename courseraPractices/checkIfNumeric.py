number = input("Enter your an integer: ")

try:
    int(number)
except ValueError as e:
    print("Input is not an integer")
    print(e)
else:
    print("Input is an integer")
