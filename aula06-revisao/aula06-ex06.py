import random  # Importa o módulo que permite gerar números aleatórios

# Solicita ao usuário o tamanho do vetor (n > 0)
n = 0
while n <= 0:
    n = int(input("Digite um número inteiro positivo para o tamanho do vetor: "))

# Cria um vetor (lista) vazio
vetor = []

# Preenche o vetor com n números aleatórios reais entre 0 e 100
for i in range(n):
    numero_aleatorio = random.uniform(0, 100)  # Gera número real entre 0 e 100
    vetor.append(numero_aleatorio)  # Adiciona o número ao vetor

# Exibe todos os números gerados
print("\nNúmeros gerados no vetor:")
for numero in vetor:
    print(numero)
