print("Digite sua idade!")

while True:
    year = int(input("Idade:"))
    if year <0 or year >100:
        print("Digite uma idade válida!")
    if year >18 and year <100:
            print("Maior de idade!")
    elif year <18:
        print("menor de idade!")
    break