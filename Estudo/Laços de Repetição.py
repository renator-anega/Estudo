print("Digite 0 para finalizar")
# zera a variável que acumula a soma
soma = 0
# para entrar no laço a primeira vez
num = 1

# início do laço Enquanto-Faça
while num != 0:
    # Bloco de repetição
    num = float(input("Digite um número: "))
    soma = soma + num

# fluxo depois do final do laço: Exibir o valor da somatória
print("Somatoria = ", soma)

# -----------------------------------------------------

# zera as variáveis dos candidatos
hug = 0
zez = 0
lui = 0

# Exibe o menu com os candidatos
print("Digite o voto ou 0 para finalizar")
print("1 – Huguinho")
print("2 – Zezinho")
print("3 – Luizinho")
print("0 – Terminar a votação")

# inicia um laço infinito
while True:
    # Lê o voto
    voto = int(input("Digite o voto: "))
    # Contabiliza o voto
    if voto == 1:
        hug = hug + 1
    elif voto == 2:
        zez = zez + 1
    elif voto == 3:
        lui = lui + 1
    else:
        if voto != 0:
            print("Voto inválido, digite: 1, 2 ou 3")

    # Este if simula a condição de saída no final do laço
    if voto == 0:
        break # força a saída do laço

# Exibe a quantidade de votos de cada candidato
print(f"1 – Huguinho: {hug} votos")
print(f"2 – Zezinho: {zez} votos")
print(f"3 – Luizinho: {lui} votos")

# -----------------------------------------------------

soma = 0
print("Digite 10 números")

# Laço configurado para 10 voltas
for i in range(1, 11, 1):
    n = float(input())
    soma = soma + n

print("Somatória = ", soma)