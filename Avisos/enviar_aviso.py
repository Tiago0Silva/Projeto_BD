def enviar_aviso(conn, cur, id):
    aviso= input("Escreva o seu aviso: ")
    QueryAviso= "INSERT INTO aviso(aviso, administrador_id) VALUES (%s ,%s)"
    try:
        cur.execute(QueryAviso, (aviso, id))
        conn.commit()
        print("")
        print("Aviso enviado com sucesso.")
        print("")
    except Exception as e:
        conn.rollback()
        print("Erro ao enviar o aviso:", e)