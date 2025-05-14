from Executes.Execute2 import execute2
from Executes.Execute1 import execute1
def login_admin(cur):
    email= input("Email: ")
    password= input("Password: ")
    
    QueryID= "SELECT id FROM administrador WHERE email= %s"
    query = "SELECT * FROM administrador WHERE email= %s AND password= %s"

    result= execute2(cur, query, email, password) is not None    
    if result:
        print("Login bem-sucedido!! Bem-vindo, ")
        ID= execute1(cur, QueryID, email)
        return ID
    else:
        print("Email ou password incorretos. Tente novamente.")