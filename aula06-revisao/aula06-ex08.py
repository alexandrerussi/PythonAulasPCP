import random  # Para gerar números aleatórios

# Solicita o número de linhas e colunas da matriz
linhas = int(input("Digite o número de linhas: "))
colunas = int(input("Digite o número de colunas: "))

# Criação das matrizes A, B e C
A = []
B = []
C = []  # Matriz soma

# Preenchimento da matriz A com inteiros aleatórios entre -10 e 10
for i in range(linhas):
    linha_A = []
    for j in range(colunas):
        valor = random.randint(-10, 10)
        linha_A.append(valor)
    A.append(linha_A)

# Preenchimento da matriz B com inteiros aleatórios entre -10 e 10
for i in range(linhas):
    linha_B = []
    for j in range(colunas):
        valor = random.randint(-10, 10)
        linha_B.append(valor)
    B.append(linha_B)

# Soma das matrizes A + B = C
for i in range(linhas):
    linha_soma = []
    for j in range(colunas):
        soma = A[i][j] + B[i][j]
        linha_soma.append(soma)
    C.append(linha_soma)

# Impressão das matrizes
print("\nMatriz A:")
for linha in A:
    print(linha)

print("\nMatriz B:")
for linha in B:
    print(linha)

print("\nMatriz Soma (C = A + B):")
for linha in C:
    print(linha)
