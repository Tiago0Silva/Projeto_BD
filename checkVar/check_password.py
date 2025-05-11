def check_password(cur, id, password):
    if not password or len(password) < 6:
        print("Mínimo de 6 caracteres!")
        return False
    else:
        Alt_password= "UPDATE utilizador SET password = %s WHERE id= %s"
        cur.execute(Alt_password, (password, id))
        return True