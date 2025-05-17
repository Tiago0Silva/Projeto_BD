from datetime import datetime
from Fundos.Saldo import Saldo
def transacao(conn, cur, categoria,titulo, tipo, id_utilizador, id_linha):
    try:
        cur.execute("BEGIN")
        cur.execute("SELECT saldo FROM utilizador WHERE id = %s FOR UPDATE", (id_utilizador,))
        saldo_atual = cur.fetchone()[0]
        Query_valor= f"SELECT {categoria} FROM precario WHERE titulo = %s AND id_linha= %s"
        Query_transacao= "INSERT INTO transacao (valor, data_hora, tipo, utilizador_id) VALUES (%s, %s, %s, %s) RETURNING id"
        Query_update_saldo = "UPDATE utilizador SET saldo = saldo - %s WHERE id = %s"
        cur.execute(Query_valor, (titulo,id_linha,))
        valor= cur.fetchone()[0]
        data_hora = datetime.now()
        
        if valor > saldo_atual:
            print("Não tens saldo suficiente!")
            return
        cur.execute(Query_update_saldo, (valor, id_utilizador))
        cur.execute(Query_transacao, (valor, data_hora, tipo, id_utilizador))
        id_transacao= cur.fetchone()[0]
        conn.commit()
        
        print(f"Transação registada.")
        return id_transacao
    
    except Exception as e:
        conn.rollback()
        print("Erro ao inserir transação:", e)