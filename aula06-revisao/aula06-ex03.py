# Validação da entrada
n = 0
while n <= 0:
    n = int(input("Digite um número inteiro positivo: "))

# Cálculo da soma
soma = 0
for i in range(1, n + 1):
    soma += i

# Impressão do resultado
print(f"A soma de 1 até {n} é: {soma}")
