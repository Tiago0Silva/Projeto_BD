from Executes.Execute1 import execute1
def Saldo(cur, id):
    QuerySal= "SELECT saldo FROM utilizador WHERE id= %s"
    saldo= execute1(cur, QuerySal, id)
    return saldo