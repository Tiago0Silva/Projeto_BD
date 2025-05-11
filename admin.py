from login_register.login.login_admin import login_admin 
from login_register.register.Register import Register
from Avisos.enviar_aviso import enviar_aviso
def admin(cur):
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
                Register(cur)
                break
            else:
                print("Opção inválida. Tente novamente.")
    finally:
        try:
            op_menu=0
            while True:
                print("1- Controlo de horários")
                print("2- Controlo de linhas")
                print("3- Preçario")
                print("4- Enviar Aviso")
                print("5- Enviar mensagem")
                print("6- Estatísticas e Relatórios")
                op_menu= int(input("Escolha: "))
                if op_menu == 4:
                    enviar_aviso(cur, loginId)
        except Exception as e:
            print("Ocorreu um erro: ", e)