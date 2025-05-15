import psycopg2
from cliente import cliente
from admin import admin
conn= psycopg2.connect("host=localhost dbname=postgres user=postgres password= postgres")
cur= conn.cursor()

#opção do tipo de conta (não deve aceitar email de admin caso a sessáo 
# escolhida não seja de admin e vice-versa)

#log_in e Register
try:
    print("1- cliente")
    print("2- Admin")
    tipo= int(input("Escolha: "))
    if tipo == 1:
        cliente(conn, cur)
    if tipo == 2:
        admin(conn, cur)
#menu de opções para admin
finally:
    cur.close()
    conn.close()