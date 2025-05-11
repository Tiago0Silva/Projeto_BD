def execute2(cur,Query, var1, var2):
    cur.execute(Query, (var1, var2))
    resposta= cur.fetchone()
    return resposta[0]