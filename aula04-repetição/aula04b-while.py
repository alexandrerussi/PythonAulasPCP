cp = 0

while cp < 3:
    print("Produto")
    cp += 1

# Primeira parte: while decrescente
i = 4
while i >= 0:
    print("Ola mundo", i)
    i -= 1

# Segunda parte: repetição com entrada do usuário
jogar = "sim"

while jogar.lower() == "sim":
    print("Repete ou inicia o jogo")
    jogar = input("Deseja jogar novamente? ")

# Terceira parte: modificadores de laço
i = 0

while i < 10:
    i += 1  # incrementa antes das verificações

    if i == 3 or i == 5:
        continue  # pula para a próxima iteração

    if i == 7:
        break  # encerra o laço

    print("Produto", i)

print("FIM")


cp = 0
while cp < 10:
    cp += 1

    if cp == 3:
        continue

    print(f"Produto {cp}")


cp = 0
while cp < 10:
    cp += 1

    if cp == 7:
        break

    print(f"Produto {cp}")
