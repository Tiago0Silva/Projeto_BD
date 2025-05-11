from Executes.Execute1 import execute1
def dados_atuais(cur, id, op):
    Queryemail= "SELECT email FROM utilizador WHERE id= %s"
    QueryNIF= "SELECT nif FROM utilizador WHERE id= %s"
    Querynome= "SELECT nome FROM utilizador WHERE id= %s"
    Querypassword= "SELECT password FROM utilizador WHERE id= %s"
    Querytelefone= "SELECT telefone FROM utilizador WHERE id= %s"
    
    try:
        while True:
            if op == "1":
                email= execute1(cur, Queryemail, id)
                print("Email antigo: ", email)
                break
            if op == "2":
                password= execute1(cur, Querypassword, id)
                print("Password antiga: ", password)
                break
            if op == "3":
                NIF= execute1(cur, QueryNIF, id)
                print("NIF antigo: ", NIF)
                break
            if op == "4":
                telefone= execute1(cur, Querytelefone, id)
                print("Telefone antigo: ", telefone)
                break
            if op == "5":
                nome= execute1(cur, Querynome, id)
                print("Nome antigo: ", nome)
                break
    except Exception as e:
        print("Ocorreu um erro: ", e)