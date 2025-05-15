def check_NIF(cur, id, NIF):
    if not (isinstance(NIF, int) and len(str(NIF))==9):
        print("NIF incorreto!")
        return False
    else:
        Alt_NIF= "UPDATE utilizador SET nif = %s WHERE id= %s"
        cur.execute(Alt_NIF, (NIF, id))
        return True