"""
Faça um programa que receba a quantidade de produtos que o usuário deseja
A seguir, seu programa deve exibir a mensagem “Produto” a
quantidade de vezes que o usuário solicitou.
Utilize o laço for.
"""

qtdProd = int(input("Digite a qtd de produtos: "))

for i in range(qtdProd):
    print(f"Produto {i}")