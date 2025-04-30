# ------------------------------
# ESTRUTURA CONDICIONAL SIMPLES
# ------------------------------

nota = 7.0

if nota < 6:
    print("Sua nota é:", nota)

print("FIM")


# ------------------------------
# ESTRUTURA CONDICIONAL COMPOSTA
# ------------------------------

nota_final = 5.0

if nota_final < 6:
    print("Reprovado")
else:
    print("Aprovado")

print("FIM")


# ------------------------------
# ESTRUTURA CONDICIONAL ENCADEADA
# ------------------------------

nota_final = 7.0

if nota_final < 4:
    print("Reprovado")
else:
    print("VAMOS VER...")

    if nota_final < 6:
        print("Recuperação")
    else:
        print("Aprovado")


# ------------------------------
# ESTRUTURA CONDICIONAL COMPOSTA V2
# ------------------------------

nota_final = 2.0

if nota_final < 4:
    print("Reprovado")
elif nota_final < 6:
    print("Recuperação")
else:
    print("Aprovado")


