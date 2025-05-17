from Precario.Gestao_precario_data import gestao_precario_data
from .Comprar import comprar
import datetime
def comprar_bilhete_passe(conn, cur, id_utilizador):
    while True:
        while True:
            print("1- Linha 1")
            print("2- Linha 2")
            print("3- Linha 3")
            print("Cada linha tem valores diferentes para a compra de bilhetes ou passes")
            linha= int(input("Selecione : "))
            if linha not in [1, 2, 3]:
                print("Insira um número válido.")
            else:
                data = datetime.date.today()
                titulo= gestao_precario_data(cur, linha, data)
                comprar(conn, cur, titulo, id_utilizador, linha)
                break   
        print("1- Sim")
        print("0- Não")
        sair= int(input("Pretende sair?"))
        if sair == 1:
            return