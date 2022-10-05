def import_and_create_dictionary(file):
    bank = {}
    f = open(file, 'r')
    lines = f.readlines()

    for line in lines:
        lst = line.strip().split(',')

        if len(lst) <= 1:
            continue

        key = lst[0].strip()
        value = lst[1].strip()

        try:
            value = float(value)
            bank[key] = bank.get(key, 0) + value
        except:
            continue

    f.close()
    return bank


print(import_and_create_dictionary('accounts.txt'))
