def check_nome(cur, id, nome):
    if not nome.strip():
        print("O nome tem de ser preenchido!")
        return False
    else:
        Alt_nome= "UPDATE utilizador SET nome = %s WHERE id= %s"
        cur.execute(Alt_nome, (nome, id))
        return True