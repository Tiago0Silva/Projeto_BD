def verifica_super(cur, id):
    Query_verificacao= "SELECT id FROM administrador WHERE super_admin = TRUE"
    cur.execute(Query_verificacao)
    super_id= cur.fetchone()
    if id == super_id[0]:
        return True
    return False