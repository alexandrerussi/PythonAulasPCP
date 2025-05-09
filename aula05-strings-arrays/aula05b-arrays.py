# Vetores (listas) em Python

# Criando uma lista de inteiros e atribuindo valores
vetor_inteiros = []
vetor_inteiros.append(10)     # adiciona 10 na posição 0
vetor_inteiros.append(1999)   # adiciona 1999 na posição 1

print("Valor inteiro na posição 0:", vetor_inteiros[0])

ano_nascimento = vetor_inteiros[1]
print("Ano nascimento:", ano_nascimento)

# acessando a posição via variável
posicao = 0
print(vetor_inteiros[posicao])

# ------------------------------------------------------------

# Lista de frutas com elementos diretamente
lista_frutas = ["Morango", "Uva", "Pera", "Tomate"]

print()
print("Fruta posição 1:", lista_frutas[1])

qtd_frutas = len(lista_frutas)
print("Qtd de frutas:", qtd_frutas)

# FOR indexado
for i in range(len(lista_frutas)):
    print(lista_frutas[i])

# Lista de números
numeros = [16, 24, 29, 33]

# FOR EACH em Python
for numero in numeros:
    print(numero)

for fruta in lista_frutas:
    print(fruta)




# Lista de números
numeros = [0, 5, 11, 4]

# FOR INDEXADO
for i in range(len(numeros)):
    print(f"Pos: {i} -- Valor: {numeros[i]}")

# FOR EACH --> percorre diretamente os valores
for num in numeros:
    print(f"Valor: {num}")