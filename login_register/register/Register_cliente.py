import psycopg2
from checkVar.checkVar import checkVar

def Register(conn,cur):
    while True:
        email = input("Email: ")
        password = input("Password: ")
        NIF = int(input("NIF: "))
        telefone = int(input("Telefone: "))
        nome = input("Nome: ")

        if checkVar(email, password, NIF, telefone, nome):
            break
    print("Registo feito!")
    
    try:
        query= "INSERT INTO utilizador (email, password, NIF, telefone, nome) VALUES (%s, %s, %s, %s, %s)"
        cur.execute(query, (email, password, NIF, telefone, nome))
        conn.commit()
    except psycopg2.Error as e:
        print("Erro ao registar no banco de dados: ", e)