def check_telefone(cur, id, telefone):
    if not (isinstance(telefone, int) and len(str(telefone))==9 and str(telefone)[0] in "29"):
        print("Telefone incorreto!")
        return False
    else:
        Alt_telefone= "UPDATE utilizador SET telefone = %s WHERE id= %s"
        cur.execute(Alt_telefone, (telefone, id))
        return True