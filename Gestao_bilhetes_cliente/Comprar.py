from datetime import datetime, date
from .Transacao import transacao
def comprar(conn, cur, titulo, id_utilizador):
    Query_insert_bilhete = "INSERT INTO bilhete_passe (categoria, data_viagem, transacao_id) VALUES (%s, %s, %s) RETURNING id"
    Query_insert_relacao = "INSERT INTO bilhete_passe_viagem (bilhete_passe_id, viagem_id) VALUES (%s, %s)"
    id_viagem= input("Insira o id da viagem que pretende: ")
    categorias_validas = ["viagem_unica", "diario", "passe_mensal", "passe_estudante", "passe_senior"]
    while True:
        categoria= input("Insira a categoria de viagem que quer: ")
        if categoria in categorias_validas:
            break
        else:
            print("Categoria inválida. Escolha uma das seguintes:", ", ".join(categorias_validas))
                    
    while True:
        data_str = input("Insira a data da viagem (formato: AAAA-MM-DD): ")
        data_viagem = datetime.strptime(data_str, "%Y-%m-%d").date()
        if data_viagem < date.today():
                print("A data não pode ser no passado.")
        else:
            break
    validacao =input("Prima 1 para validar a compra: ")
    if validacao != '1':
        print("Compra cancelada.")
        return
    tipo='Compra'
    id_transacao= transacao(conn, cur, categoria,titulo, tipo, id_utilizador)
    if id_transacao is None:
        print("Falha ao criar transação.")
        return
    
    try:

        cur.execute(Query_insert_bilhete, (categoria,data_viagem, id_transacao))
        id_bilhete = cur.fetchone()[0]

        cur.execute(Query_insert_relacao, (id_bilhete, id_viagem))

        conn.commit()
        print("Compra efetuada com sucesso.")

    except Exception as e:
        conn.rollback()
        print("Erro ao finalizar compra:", e)