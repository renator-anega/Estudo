lista = []
soma = 0
for i in range(0,10,1):
    x = float(input("Digite 10 números para somar: "))
    lista.append(x)
    soma = soma + x
for elem in lista:
    print(elem)
print(f"A somátoria da lista é: {soma:.2f}")