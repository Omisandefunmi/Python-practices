print('4 * 4 = ', 4*4)
print('4 * 4 = ', str(4*4))
print('is 4 an even number? ', 4 % 2 == 0)
print('is 4 an even number? ' + str(4 % 2 == 0))

fav_movie = (input("what is your favourite movie: "))

fav_artist = (input("who is your favourite singer: "))

text = 'Your favourite movie is {} and your favourite artist is {}'.format(fav_movie, fav_artist)

print(text)

#Ask for age and add 3 years, print the result

age = int(input("How old are you? "))
print('You will be '+(str(age + 3))+ " in 3 years")
