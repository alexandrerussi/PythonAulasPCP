# Atribuição	de	tuplas
#Muitas	vezes,	é	útil	trocar	os	valores	de	duas	variáveis.
# Com	a	atribuição	convencional,	é  preciso	usar	uma	variável temporária.
# Por	exemplo,	trocar	a	e	b

a = 5
b = 10
print(f"a: {a}, b: {b}")

temp = a
a =	b
b =	temp
print(f"a: {a}, b: {b}")

a = 5
b = 10
print(f"a: {a}, b: {b}")

a, b = b, a
print(f"a: {a}, b: {b}")


# De	forma	geral,	o	lado	direito	pode	ter	qualquer
# tipo	de	sequência	(string,	lista	ou	tupla).

#  Por	exemplo,	para	dividir	um	endereço	de	email	em
#  um	nome	de	usuário	e	um	domínio,  você	poderia	escrever:

addr = 'monty@python.org'
uname, domain = addr.split('@')

print(uname)
print(domain)