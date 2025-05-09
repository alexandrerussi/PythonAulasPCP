nomes = ["Ana", "Bia", "Rodrigo", "Bruno"]

# Parte 1: fixar o primeiro nome ("Ana") e formar duplas com os demais
nome_temporario = nomes[0]  # Ana (fixado)

for i in range(1, len(nomes)):
    print(f"{nome_temporario}, {nomes[i]}")

print()

nomes = ["Ana", "Bia", "Rodrigo", "Davi"]
for j in range(len(nomes) - 1):
    nome_temp = nomes[j]
    for i in range(j + 1, len(nomes)):
        print(f"{nome_temp}, {nomes[i]}")