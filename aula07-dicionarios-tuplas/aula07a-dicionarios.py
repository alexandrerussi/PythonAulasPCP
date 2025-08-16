eng2sp = dict()
print(eng2sp)

eng2sp['one'] = 'uno'
print(eng2sp)

eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)
print(eng2sp['two'])

# print(eng2sp['four'])
print(len(eng2sp))

# O	operador	in	funciona	em	dicionários	também;
# ele	acusa	se	algo  aparece	como	chave	no
# dicionário	(aparecer	como	valor	não	é	o	suficiente).

print('one' in eng2sp)
print('uno' in eng2sp)

# Para	ver	se	algo	aparece	como	um	valor	em	um	dicionário,
# você	pode	usar	o	método
# values,	que	devolve	uma	coleção	de	valores,
# e	então	usar	o	operador	in:

vals = eng2sp.values()
print('uno' in vals)

def	count_letters(s):
    d =	dict()
    for	c in s:
        if c not in	d:
            d[c] = 1
        else:
            d[c] +=	1
    return	d

count = count_letters("paralelepipedo")
print(count)

def	print_count(h):
    for	c in h:
        print(c, h[c])

print_count(count)