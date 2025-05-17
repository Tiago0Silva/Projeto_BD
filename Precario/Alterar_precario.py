from Precario.Valor_alterado import valor_alterado
def alterar_precario(conn, cur):
    print("Linha a alterar:")
    print("1- linha1")
    print("2- linha2")
    print("3- linha3")
    linha= int(input("Escolha: "))
    
    print("")
    print("1- Viagem Única")
    print("2- Diário")
    print("3- Passe Mensal")
    print("4- Passe Estudante")
    print("5- Passe Sénior")
    categoria= int(input("Escolha: "))
    valor_alterado(conn, cur, linha,  categoria)