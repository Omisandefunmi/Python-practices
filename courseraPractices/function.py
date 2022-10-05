def letter_grade():
    grade = int(input("Enter your grade: "))

    if grade >= 90:
        print("A")
    elif grade >= 70:
        print('B')
    elif grade >= 50:
        print("C")
    else:
        print("F")


print(letter_grade())
