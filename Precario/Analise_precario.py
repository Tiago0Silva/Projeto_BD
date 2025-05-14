from Controlo_linhas.Visualizar_tabela import visualizar_tabela
from .Alterar_precario import alterar_precario
def analise_precario(cur):
    Query_precario1= "SELECT viagem_unica, diario, passe_mensal, passe_estudante, passe_senior FROM precario WHERE id_linha = 1"
    Query_precario2= "SELECT viagem_unica, diario, passe_mensal, passe_estudante, passe_senior FROM precario WHERE id_linha = 2"
    Query_precario3= "SELECT viagem_unica, diario, passe_mensal, passe_estudante, passe_senior FROM precario WHERE id_linha = 3"
    
    print(" ")
    print("Linha 1:")
    cur.execute(Query_precario1)
    linha1= cur.fetchall()
    visualizar_tabela(cur, linha1)
    print(" ")
    print("Linha 2:")
    cur.execute(Query_precario2)
    linha2= cur.fetchall()
    visualizar_tabela(cur, linha2)
    print(" ")
    print("Linha 3:")
    cur.execute(Query_precario3)
    linha3= cur.fetchall()
    visualizar_tabela(cur, linha3)
    print(" ")
    while True:
        print("Deseja alterar agum valor de um bilhete?")
        print("1- Sim")
        print("0- Não")
        selecionado= int(input("Escolha: "))
        if selecionado == 1:
            alterar_precario(cur)
            break
        if selecionado == 0:
            break