from Executes.Execute3 import execute3
from datetime import datetime

def enviar_aviso(cur, id):
    print("Escreva o seu aviso:")
    aviso= input("")
    data_hora = datetime.now()
    QueryAviso= "INSERT INTO aviso(data_hora, mensagem, administrador_id) VALUES (%s ,%s, %s)"
    execute3(cur,QueryAviso, data_hora, aviso, id)
