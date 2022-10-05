person = {'name': 'Eugene', 'height': '2.7cm', 'married': True, 'sibling': ['wendy', 'sandy']}

print(type(person))

print(person.get('name'))

# person.update('friends')
print(person)
person.__delitem__('name')
print(person)
person.update([('hobby', 'ball')])
# person['hobby'] = 'ball'
print(person)

new_dict = {"A": "Apple", "B": "Ball", "C": "Cat"}
keys = new_dict.keys()

for k in keys:
    print(k, ':', new_dict[k], end=', ')

