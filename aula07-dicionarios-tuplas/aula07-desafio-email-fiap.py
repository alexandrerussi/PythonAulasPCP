# Desafio: Analisador de E-mails da FIAP

# 1️⃣ Entrada dos e-mails
emails_input = input("Digite os e-mails separados por vírgula: ")

# 2️⃣ Quebrar a string em uma lista, removendo espaços extras
emails_lista = [email.strip() for email in emails_input.split(",")]

# Dicionário para contar quantos e-mails por domínio
dominios_count = {}

# Lista para armazenar os nomes de usuário
usuarios = []

# 3️⃣ Processar cada e-mail
for email in emails_lista:
    # Separar nome de usuário e domínio
    usuario, dominio = email.split("@")
    usuarios.append(usuario)

    # Contar domínios
    if dominio not in dominios_count:
        dominios_count[dominio] = 1
    else:
        dominios_count[dominio] += 1

# 4️⃣ Converter a lista de usuários para tupla
usuarios_tuple = tuple(usuarios)

# 5️⃣ Trocar o primeiro e o último usando atribuição de tupla
usuarios_lista_trocados = list(usuarios_tuple)
usuarios_lista_trocados[0], usuarios_lista_trocados[-1] = usuarios_lista_trocados[-1], usuarios_lista_trocados[0]
usuarios_tuple_trocados = tuple(usuarios_lista_trocados)

# 6️⃣ Exibir relatório final
print("\n📊 Relatório:")
print("- Quantidade de e-mails por domínio:")
for dominio, qtd in dominios_count.items():
    print(f"  {dominio}: {qtd}")

print(f"- Lista de usuários: {usuarios_tuple}")
print(f"- Após troca de posições: {usuarios_tuple_trocados}")
