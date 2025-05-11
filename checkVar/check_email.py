import re 
def check_email(cur, id, email):
    email_check= r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_check, email):
        print("email inválido!")
        return False
    else:
        Alt_email= "UPDATE utilizador SET email = %s WHERE id= %s"
        cur.execute(Alt_email, (email, id))
        return True