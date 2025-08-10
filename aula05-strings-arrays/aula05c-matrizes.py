pessoas = [
    ["Fernando", 25, "123.456.789-00"],
    ["Rodrigo", 35, "223.456.789-00"],
    ["Joaquina", 45, "323.456.789-00"]
]

# pessoas[linha][coluna]
print(pessoas[0][1])
maiorTemp = 0
for pessoa in pessoas:
    for info in pessoa:
        print(info)
    print()