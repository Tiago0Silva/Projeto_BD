def execute1(cur,Query, var):
    cur.execute(Query, (var,))
    resposta= cur.fetchone()
    return resposta[0]