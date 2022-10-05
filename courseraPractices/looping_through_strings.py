planets = ['Venus', 'Jupiter', 'Mercury', 'Sun', 'Earth']

for planet in planets:
    if planet == 'Sun':
        print(planet, "is not a planet")
    else:
        print(planet, "is a planet")
    if planet == 'Mercury':
        print(planet, 'is closer to the sun')

month = 'September'
print(month, 'is spelled: ')
for letter in month:
    print(letter)

month = 'September'
print(month, 'is spelled: ')
for letter in month:
    print(letter, end=' ')
print()

name = input("what is your name? ")

letter_count = 0
print(name, "is spelled")
for letter in name:
    letter_count += 1
    print(letter, end=' ')
print()
print(name, 'contains', letter_count, 'letters')



