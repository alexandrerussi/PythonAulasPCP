escolha_usuario = 0

match escolha_usuario:
    case 0:
        status = "Sair do programa"
    case 1:
        status = "Entrar no programa"
    case _:
        status = "Erro"

print(status)


nota_final = 7.0

prep1 = nota_final >= 5     # True
prep2 = nota_final < 7      # False

logica_e = prep1 and prep2  # False
logica_ou = prep1 or prep2  # True



