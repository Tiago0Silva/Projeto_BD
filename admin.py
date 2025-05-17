from login_register.login.login_admin import login_admin 
from login_register.register.Register_admin import register_admin
from Avisos.enviar_aviso import enviar_aviso
from Controlo_linhas.controlo_linhas import controlo_linha
from Precario.Analise_precario import analise_precario
from Gerir_Admins.Verifica_super import verifica_super
from Gerir_Admins.Gerir_admins import gerir_admins
from Gestao_bilhetes_cliente.Reembolsos_cancelamentos import reembolsos_cancelamentos
from Gestao_bilhetes_cliente.Notificacao_cancelamentos import notificacao_cancelamentos
def admin(conn,cur):
    
    try:
        Log_Reg=0
        while True:
            print("1- Login")
            print("2- Registar")
            Log_Reg= input("Digite 1 para login ou 2 para registar: ")

            if Log_Reg == "1":
                loginId= login_admin(cur)
                break
            elif Log_Reg == "2":
                register_admin(conn, cur)
                break
            else:
                print("Opção inválida. Tente novamente.")
    finally:
        try:
            op_menu=0
            while True:
                print("1- Gestão de linhas") #:)
                print("2- Preçario") #:)
                print("3- Enviar Aviso") #:)
                print("4- Enviar mensagem")
                print("5- Reembolsos e cancelamentos", notificacao_cancelamentos(cur)) #:)
                print("6- Estatísticas e Relatórios")
                if verifica_super(cur, loginId):
                    print("7- Gerir Permissões") #:)
                print("0- LogOut") #:)
                op_menu= int(input("Escolha: "))
                
                if op_menu == 1:
                    controlo_linha(conn, cur)
                if op_menu == 2:
                    analise_precario(cur)
                if op_menu == 3:
                    enviar_aviso(conn, cur, loginId)
                if op_menu == 5:
                    reembolsos_cancelamentos(conn, cur)
                if op_menu == 7 and verifica_super(cur, loginId):
                    gerir_admins(conn, cur)
                if op_menu == 0:
                    break
        except Exception as e:
            print("Ocorreu um erro: ", e)