def notificacao(cur):
    query = "SELECT COUNT(*) FROM utilizador_aviso WHERE lido = FALSE"
    cur.execute(query)
    n_not = cur.fetchone()
    
    not_str = f"({n_not[0]})"
    return not_str
