# LÓGICA E (and)
# EMAIL    SENHA   LOGIN
# true     true    true
# true     false   false
# false    true    false
# false    false   false

verifica_email = False
verifica_senha = False

verifica_login = verifica_email and verifica_senha
print(verifica_login)

if verifica_login:
    print("Entrar no programa")

# LÓGICA OU (or)
# SOL NO DOM   JOGO BR    CHURRASCO NO DOM.
# true         true        true
# true         false       true
# false        true        true
# false        false       false

logica_ou = False or False
print(logica_ou)

# OPERADOR DE NEGAÇÃO

negacao = not False
print(negacao)

if not verifica_login:
    print("loga aí")