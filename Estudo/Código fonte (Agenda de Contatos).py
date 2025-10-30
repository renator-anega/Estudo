
# Código
agenda = []

def add():
    global agenda
    print("Registre seu novo contato")
    nome = p_nome()
    cll = input("Celular: ")
    email = str(input("Email: "))
    agenda.append([nome, cll, email])


def p_nome():
    return(input("nome: "))

def listar_dados(nome, celular, email):
    print("nome: %s\nCelular: %s\nEmail: %s" % (nome, celular, email))

def listar():
    print("CONTATOS DA AGENDA")
    for e in agenda:
        listar_dados(e[0], e[1], e[2])
    print("FIM DA AGENDA")

def pesquisa(nome):
    name = nome.lower()
    for d, e in enumerate(agenda):
        if e[0].lower() == name:
            return d
        return None
    
def pesquisar():
    p = pesquisa(p_nome())
    if p != None:
        print("Registro encontrado!")
        nome = agenda[p][0]
        celular = agenda[p][1]
        email = agenda[p][2]
        listar_dados(nome, celular, email)
    else:
        print("nome não encontrado!!!")
def apagar():
    global agenda
    nome = p_nome()
    p = pesquisa(nome)
    if p != None:
        del agenda[p]
        print("Registro apagado com sucesso.")
    else:
        print("nome não encontrado.")
def editar():
    p = pesquisa(p_nome())
    if p != None:
        nome = agenda[p][0]
        print(f"nome: {nome} ")
        celular = input("Celular: ")
        email = input("Email: ")
        agenda[p] = [nome, celular, email]
        print("Regristo editado com sucesso! ")
    else:
        print("nome não encontrado!")
def validar(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return(valor)
            else:
                return(0)
        except ValueError:
            print(f"Valor inválido, favor digitar entre {inicio} e {fim}")
def menu():
    print("""
          1 - Adicionar novo contato 
          2 - Editar um contato 
          3 - Pesquisar contato 
          4 - Lista de contatos 
          5 - Apagar um contato 
          6 - Sair 
          """)
    return validar("Escolha uma opção:", 1, 6)

while True:  # Criando um loop infinito.
    opcao = menu()
    if opcao == 0:
        print("Opcao Inválida!")
    elif opcao == 6:
        print("Adeus!")
        break
    elif opcao == 1:
        add()
    elif opcao == 2:
        editar()
    elif opcao == 3:
        pesquisar()
    elif opcao == 4:
        listar()
    elif opcao == 5:
        apagar() 