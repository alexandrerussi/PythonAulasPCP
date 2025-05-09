# MATRIZES EM PYTHON

# Tabuleiro do jogo da velha (3x3)
tabuleiro = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

tabuleiro[0][0] = 'X'
tabuleiro[1][1] = 'O'
tabuleiro[2][2] = 'X'

print("\nTabuleiro:")
for linha in tabuleiro:
    print(" | ".join(linha))
