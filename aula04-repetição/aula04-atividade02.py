"""
Em muitos dos nossos algoritmos fizemos validações dos dados de entrada.
Contudo, apenas exibíamos mensagens e encerrávamos nossos algoritmos.
Com os comandos de repetição temos condições de garantir que a informação esteja correta antes do algoritmo continuar.

Atividade 4: Escreva um programa que dadas duas notas de 0 a 10 calcula a média aritmética entre elas.
"""

# Solicita e valida a primeira nota
nota1 = float(input("Digite a primeira nota: "))
while nota1 < 0 or nota1 > 10:
    print("A nota deve estar entre 0 e 10.")
    nota1 = float(input("Digite a primeira nota: "))

# Solicita e valida a segunda nota
nota2 = float(input("Digite a segunda nota: "))
while nota2 < 0 or nota2 > 10:
    print("A nota deve estar entre 0 e 10.")
    nota2 = float(input("Digite a segunda nota: "))

# Calcula e exibe a média
media = (nota1 + nota2) / 2
print(f"A média é: {media}")
