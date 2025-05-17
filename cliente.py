from login_register.login.login_cliente import login_cliente
from login_register.register.Register_cliente import Register
from Fundos.Fundos_Carteira import Fundos_Carteira
from Informacoes_pessoais.Info_pessoal import Info_pessoal
from Avisos.notificacao import notificacao
from Avisos.ler_avisos import ler_avisos
from Gestao_bilhetes_cliente.Compra_bilhete_passe import comprar_bilhete_passe
from Gestao_bilhetes_cliente.Gerir_bilhetes import gerir_bilhetes
def cliente(conn, cur):
    try:
        Log_Reg=0
        while True:
            print("1- Login")
            print("2- Registar")
            Log_Reg= input("Digite 1 para login ou 2 para registar: ")

            if Log_Reg == "1":
                loginId= login_cliente(cur)
                break
            elif Log_Reg == "2":
                Register(conn, cur)
            else:
                print("Opção inválida. Tente novamente.")

    finally:
        try:
            opmenu= 0
            while True:
                print("1- Informações pessoais")# :)
                print("2- Carteira")# :)
                print("3- Comprar bilhetes/passes") #:)
                print("4- Gerir bilhetes e passes") #:)
                print("5- Avisos", notificacao(cur)) #:)
                print("0- LogOut")# :)
                opmenu=int(input("Escolha..."))

                if opmenu == 1:
                    Info_pessoal(cur, loginId)
                if opmenu == 2:
                    Fundos_Carteira(conn, cur, loginId)
                if opmenu == 3:
                    comprar_bilhete_passe(conn, cur, loginId)
                if opmenu == 4:
                    gerir_bilhetes(conn, cur, loginId)
                if opmenu == 5:
                    ler_avisos(cur, loginId)
                if opmenu == 0:
                    break
        except Exception as e:
            print("Ocorreu um erro: ", e)