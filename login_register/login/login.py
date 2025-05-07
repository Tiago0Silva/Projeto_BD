import psycopg2

def login(cur):
    email= input("Email: ")
    password= input("Password: ")
    
    query = "SELECT * FROM Utilizador WHERE email= %s AND password= %s"
    cur.execute(query, (email, password))
    result= cur.fetchone() is not None
    
    if result:
        QueryNome= "SELECT nome,id FROM Utilizador WHERE email= %s"
        QueryID= "SELECT id FROM utilizador WHERE email= %s"
        
        cur.execute(QueryNome, (email,))
        Nome= cur.fetchone()
        print("Login bem-sucedido!! Bem-vindo, ", Nome[0],)
        
        cur.execute(QueryID, (email,))
        IDtone= cur.fetchone()
        ID=IDtone[0]
        return ID
    else:
        print("Email ou password incorretos. Tente novamente.")