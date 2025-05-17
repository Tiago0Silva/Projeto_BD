def notificacao_cancelamentos(cur):
    query = "SELECT COUNT(*) FROM pedido_gestao_bilhetes_passes WHERE estado_aceitacao = 'por avaliar'"
    cur.execute(query)
    n_not = cur.fetchone()
    
    not_str = f"({n_not[0]})"
    return not_str