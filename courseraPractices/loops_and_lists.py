items = ['1', 3, 'car', 0, 'tree']

for item in items:
    print(item)

print(len(items))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)
print("There are", len(even_numbers), "even numbers in the list of numbers")

x = 0
for x in range(5):
    if x == 3:
        continue
    print(x)


