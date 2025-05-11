def execute3(cur,Query, var1, var2,var3):
    cur.execute(Query, (var1, var2, var3))
    resposta= cur.fetchone()
    return resposta[0]