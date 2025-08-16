t = 'a', 'b', 'c', 'd', 'e'
t = ('a', 'b', 'c', 'd', 'e')

# tupla unico elemento
t1 = 'a',
print(type(t1))

# Um	único	valor	entre	parênteses	não	é	uma	tupla:
t2 = ('a')
print(type(t2))

#Outra	forma	de	criar	uma	tupla	é	com	a	função	integrada	tuple.
# Sem	argumentos,	cria  uma	tupla	vazia:
t = tuple()

#Se	os	argumentos	forem	uma	sequência	(string,	lista	ou	tupla),
# o	resultado	é	uma	tupla  com	os	elementos	da	sequência:
t = tuple('lupins')
print(t)

# A	maior	parte	dos	operadores	de	lista	também	funciona	em	tuplas.
# O	operador	de  colchetes	indexa	um	elemento:
t = ('a', 'b', 'c', 'd', 'e')
print(t[0])
print(t[1:3])

 #Entretanto,	se	tentar	alterar	um	dos	elementos	da	tupla,
# vai	receber	um	erro:
# t[0] = 'A'

#Como	tuplas	são	imutáveis,	você	não	pode	alterar	os	elementos,
# mas	pode	substituir	uma  tupla	por	outra:
t = ('A',) + t[1:]
print(t)