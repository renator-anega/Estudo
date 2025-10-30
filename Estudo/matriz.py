# Manipulando a matriz
matrizes = [ [0,0], [0,0], [0,0], [0,0] ]

# Preenchendo a matriz
print("Preenchendo a matriz...")
for l in range(4):
    for c in range(2):
        matrizes[l][c] = int(input(f"Matriz[{l}][{c}]= "))

# Exibir a matriz
for l in range(4):
    for c in range(2):
        print(f"{matrizes[l][c]}\t", end = "")
    print()

# Soma dos elementos da matriz
soma = 0
for l in range(4):
    for c in range(2):
        soma = soma + matrizes[l][c]
print(soma)

# Procurando valor na matriz
while True:
    achou = float(input("Digite um valor: "))
    if achou == True:
        print(f"Valor {achou} localizado!")
        break
    else:
        print("Valor não encontrado")