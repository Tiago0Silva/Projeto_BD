from datetime import datetime
def transacao(conn, cur, categoria,titulo, tipo, id_utilizador):
    try:
        Query_valor= f"SELECT {categoria} FROM precario WHERE titulo = %s"
        Query_transacao= "INSERT INTO transacao (valor, data_hora, tipo, utilizador_id) VALUES (%s, %s, %s, %s) RETURNING id"
        cur.execute(Query_valor, (titulo,))
        valor= cur.fetchone()
        data_hora = datetime.now()
        cur.execute(Query_transacao, (valor[0], data_hora, tipo, id_utilizador))
        id_transacao= cur.fetchone()[0]
        conn.commit()
        
        print(f"Transação registada.")
        return id_transacao
    
    except Exception as e:
        conn.rollback()
        print("Erro ao inserir transação:", e)