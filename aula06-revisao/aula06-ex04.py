# Entrada do número positivo
n = int(input("Digite um número inteiro positivo: "))

# Impressão dos divisores
print(f"Divisores de {n}:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
