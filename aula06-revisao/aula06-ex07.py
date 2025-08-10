# Solicita ao usuário um número inteiro positivo para definir o tamanho do vetor
n = 0
while n <= 0:
    n = int(input("Digite o número de posições do vetor (n > 0): "))

# Criação e preenchimento do vetor de caracteres
vetor = []

print("Digite os caracteres (um por vez):")
for i in range(n):
    caractere = input(f"Posição {i}: ")
    vetor.append(caractere)

# Exibe o vetor original
print("\nVetor original:", vetor)

# Inversão manual do vetor (trocando elementos da ponta para o centro)
for i in range(n // 2):
    # Troca os elementos das extremidades
    temp = vetor[i]
    vetor[i] = vetor[n - 1 - i]
    vetor[n - 1 - i] = temp

# Exibe o vetor invertido
print("Vetor invertido:", vetor)
