print("Olá, Mundo!")

print(7+4)

print("7"+"4")

# Comentários em python
'''
    Comentarios de múltiplas linhas
'''

# Variáveis

# nome recebe 'Alexandre'
nome = 'Alenxandre'
idade = 25
peso = 65


# print(nome + idade + peso) ERRADO
print(nome, idade, peso)


nome = input('Qual é o seu nome? ')
idade = input("Quantos anos você tem? ")
peso = input('Qual é o seu peso? ')

print(nome, idade, peso)

# Tipos primitivos

n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro: "))

print(type(n1))
soma = n1 + n2

# print("A soma entre", n1, "e", n2, "vale", soma)
print("A soma entre {} e {} vale {}".format(n1, n2, soma))

print("A subtração entre {} e {} vale {}".format(n1, n2, n1-n2))

numFloat = float(input("Digite um valor: "))
print(numFloat)


text = input("Digite um valor: ")
print(text.isalnum())

# conversão de variáveis:
# https://www.digitalocean.com/community/tutorials/how-to-convert-data-types-in-python-3-pt