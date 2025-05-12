def limpar_cursor(cur):
    if cur.description:
        try:
            cur.fetchall()
        except:
            pass
