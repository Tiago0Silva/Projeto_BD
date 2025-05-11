import psycopg2
from checkVar.checkVar import checkVar

def register_admin(cur):
    while True:
        email = input("Email: ")
        password = input("Password: ")
        
        if checkVar(email, password):
            break
    print("Registo feito!")
    
    try:
        query= "INSERT INTO administrator (email, password) VALUES (%s, %s)"
        cur.execute(query, (email, password))
        cur.connection.commit()
    except psycopg2.Error as e:
        print("Erro ao registar no banco de dados: ", e)