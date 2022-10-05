def count_vowels(string):
    vowel_count = 0
    for char in string:
        if char in 'aeiou':
            vowel_count += 1
    return vowel_count


def word_count(sentence):
    space_count = 0
    sentence.strip()
    for char in sentence:
        if char in ' ':
            space_count += 1
    word_counter = space_count + 1
    return word_counter


def get_factor(x):
    factors = []
    i = 1
    while i <= x:
        if x % i == 0:
            factors.append(i)
            # decrementing i
        i += 1
    return factors


print(get_factor(9))
