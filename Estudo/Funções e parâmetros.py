# Criação da função sem parâmetro
def pi():
    return 3.1415;

# Chamada da função
print ("PI = ", pi())

# -----------------------------------------------------

# Criação da função com parâmetro
def maior2n(num1, num2):
    if num1 > num2:
        maior = num1
    else:
        maior = num2
    return maior

# Programa principal
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
print("Maior numero: ", maior2n(n1,n2))

# -----------------------------------------------------

# Criação do procedimento
def saudacao():
    print("Olá Usuário, você está logado")

# Chamada do procedimento
saudacao()

# -----------------------------------------------------

# Criação do procedimento com parâmetros
def saudacao2(usuario, hora):
    if hora < 12:
        msg = "Bom dia!"
    elif hora < 18:
        msg = "Boa tarde!"
    else:
        msg = "Boa noite!"
    print("Olá "+ usuario +", "+ msg +" Você está logado")

# Chamada do procedimento
saudacao2("Edson", 16)