from checkVar.check_email import check_email
from checkVar.check_password import check_password
from checkVar.check_NIF import check_NIF
from checkVar.check_telefone import check_telefone
from checkVar.check_nome import check_nome
from Fundos.Saldo import Saldo
from Dados_atual.dados_atuais import dados_atuais
def Info_pessoal(cur, id):
    saldo= Saldo(cur, id)
    print("Saldo: ", saldo)
    print("1- Alterar email")
    print("2- Alterar password")
    print("3- Alterar NIF")
    print("4- Alterar telefone")
    print("5- Alterar nome")
    print("6- Voltar ao menu principal")
    op_alterar= input("Escolha --> ")
    try:
        while True:
            if op_alterar == "1":
                while True:
                    dados_atuais(cur, id, op_alterar)
                    email= input("Insira o novo email: ")
                    if check_email(cur, id, email):
                        print("Email alterado para ", email)
                        break
            if op_alterar == "2":
                while True:
                    dados_atuais(cur, id, op_alterar)
                    password= input("Insira uma nova password: ")
                    if check_password(cur, id, password):
                        print("Password alterada para ", password)
                        break
            if op_alterar == "3":
                while True:
                    dados_atuais(cur, id, op_alterar)
                    NIF= int(input("Altere o NIF: "))
                    if check_NIF(cur, id, NIF):
                        print("NIF alterado para ", NIF)
                        break
            if op_alterar == "4":
                while True:
                    dados_atuais(cur, id, op_alterar)
                    telefone= int(input("Altere o numero de telemovel: "))
                    if check_telefone(cur, id, telefone):
                        print("Telefone alterado para ", telefone)
                        break
            if op_alterar == "5":
                while True:
                    dados_atuais(cur, id, op_alterar)
                    nome= input("Altere o seu nome: ")
                    if check_nome(cur, id, nome):
                        print("Nome alterado para ", nome)
                        break
            if op_alterar == "6":
                break
            
            break
            
    except Exception as e:
        print("Ocorreu um erro: ", e)
        