from Executes.Execute2 import execute2
from Executes.Execute1 import execute1
def login_admin(cur):
    email= input("Email: ")
    password= input("Password: ")
    
    QueryNome= "SELECT nome,id FROM administrator WHERE email= %s"
    QueryID= "SELECT id FROM administrator WHERE email= %s"
    query = "SELECT * FROM administrator WHERE email= %s AND password= %s"

    result= execute2(cur, query, email, password) is not None    
    if result:
        Nome= execute1(cur, QueryNome, email)
        print("Login bem-sucedido!! Bem-vindo, ", Nome[0],)
        ID= execute1(cur, QueryID, email)
        
        return ID
    else:
        print("Email ou password incorretos. Tente novamente.")