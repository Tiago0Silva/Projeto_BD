import psycopg2
from cliente import cliente
from admin import admin
conn= psycopg2.connect("host=localhost dbname=postgres user=postgres password= postgres")
cur= conn.cursor()

try:
    print("1- cliente")
    print("2- Admin")
    tipo= int(input("Escolha: "))
    if tipo == 1:
        cliente(conn, cur)
    if tipo == 2:
        admin(conn, cur)
finally:
    cur.close()
    conn.close()