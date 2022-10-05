def capitalize_or_join(sentence):
    sent = sentence.strip()
    if sent.startswith('*'):
        sent_ = sent.replace('*', '')
        split_ = sent_.split()
        result = ''
        for i in split_:
            i = i.replace(i[0], i[0].capitalize())
            i = i.replace(i[-1], i[-1].capitalize())
            result += i
            result += ' '
        return result.strip()
    else:
        result2 = sent.split()
        result3 =''
        for word in result2:
            result3.join(word)
        return result3
    return


sample = "  *ayoba has med"
samp = " ayoba has med"
sampl = " ayoba has   med"
# print(capitalize_or_join(sample))
print(capitalize_or_join(samp))
print(capitalize_or_join(sampl))
