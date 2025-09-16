def count_letters(s):
    d = {}
    for letra in s:
        if letra in d:
            d[letra] += 1
        else:
            d[letra] = 1
    return d

print(count_letters("banana"))