# Vamos percorrer os números de 2 até 2000 (inclusive)
for numero in range(2, 2001):
    # Inicialmente, assumimos que o número é primo
    primo = True

    # Agora testamos se o número tem algum divisor além de 1 e ele mesmo
    # Vamos testar de 2 até numero-1
    for divisor in range(2, numero):
        if numero % divisor == 0:
            # Se o número for divisível por qualquer outro, ele NÃO é primo
            primo = False
            break  # não precisa testar mais, já sabemos que não é primo

    # Se ao final da verificação, o número ainda for considerado primo:
    if primo:
        print(numero)
