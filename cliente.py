from login_register.login.login_cliente import login_cliente
from login_register.register.Register_cliente import Register
from Fundos.Fundos_Carteira import Fundos_Carteira
from Informacoes_pessoais.Info_pessoal import Info_pessoal
from Avisos.notificacao import notificacao
from Avisos.ler_avisos import ler_avisos
from Gestao_bilhetes_cliente.Compra_bilhete_passe import comprar_bilhete_passe
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
                Register(cur)
            else:
                print("Opção inválida. Tente novamente.")

#menu de opções para cliente
    finally:
        try:
            opmenu= 0
            while True:
                print("1- Informações pessoais")# :)
                print("2- Carteira")# :)
                print("3- Comprar bilhetes/passes") #todas as linhas e horários disponíveis e filtrar os mesmos e adquirir bilhetes ou passes
                print("4- Gerir bilhetes e passes") #ver todos os bilhetes comprados e altertar o estado para usado gerir/cancelar bilhetes/passes
                print("5- Avisos", notificacao(cur)) #:)
                print("0- LogOut")# :)
                opmenu=int(input("Escolha..."))

                if opmenu == 1:
                    Info_pessoal(cur, loginId)
                if opmenu == 2:
                    Fundos_Carteira(cur, loginId)
                if opmenu == 3:
                    comprar_bilhete_passe(conn, cur, loginId)
                #if opmenu == 4:
                    #Gerir Bilhetes
                if opmenu == 5:
                    ler_avisos(cur, loginId)
                if opmenu == 0:
                    break
        except Exception as e:
            print("Ocorreu um erro: ", e)