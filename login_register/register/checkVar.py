import re
import psycopg2

def checkVar(email, password, NIF, telefone, nome):
    
    if not (isinstance(NIF, int) and len(str(NIF))==9):
        print("NIF incorreto!")
        return False
    if not (isinstance(telefone, int) and len(str(telefone))==9 and str(telefone)[0] in "29"):
        print("NIF incorreto!")
        return False
    if not nome.strip():
        print("O nome tem de ser preenchido!")
        return False
    if not password or len(password) < 6:
        print("Mínimo de 6 caracteres!")
        return False
    email_check= r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_check, email):
        print("email inválido!")
        return False
    
    return True