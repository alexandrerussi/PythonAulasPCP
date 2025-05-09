
# Criando uma matriz 4x5 preenchida com números de 1 a 20
linhas = 4
colunas = 5

matriz = []
numero = 1

# Preenchendo a matriz
for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(numero)
        numero += 1
    matriz.append(linha)

# Exibindo a matriz
print("\nMatriz 4x5:")
for linha in matriz:
    print("\t".join(str(num) for num in linha))
