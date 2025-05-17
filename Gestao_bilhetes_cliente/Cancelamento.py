def cancelamento(conn, cur,id_utilizador, id_bilhete_passe):
    Tipo_Pedido= 'Cancelamento'
    Query_pedido_cancelamento= "INSERT INTO pedido_gestao_bilhetes_passes(tipo_pedido, id_bilhete_passe, justificacao, utilizador_id) VALUES(%s, %s, %s, %s)"
    try:
        justificacao = input("Justifique o cancelamento: ").strip()
        if not justificacao or len(justificacao) < 8:
            raise ValueError("Justificação deve ter pelo menos 10 caracteres")
    
        cur.execute(Query_pedido_cancelamento, (Tipo_Pedido, id_bilhete_passe, justificacao, id_utilizador,))
        conn.commit()
        print("Pedido de cancelamento registado com sucesso!")
    except ValueError as ve:
        conn.rollback()
        print(f"Erro de validação: {ve}")