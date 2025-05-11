from Executes.Execute1 import execute1
def ler_avisos(cur, id):
    Query_id_aviso= "SELECT aviso_id FROM utilizador_aviso WHERE utilizador_id= %s AND lido= FALSE"
    Query_n= "SELECT COUNT (*) FROM utilizador_aviso WHERE utilizador_id = %s AND lido = FALSE"
    Queryaviso= "SELECT mensagem FROM aviso WHERE id= %s"
    
    cur.execute(Query_n, (id ,))
    n= cur.fetchone()[0]
    i=0
    if n > 0:
        cur.execute(Query_id_aviso, (id,))
        id_aviso= cur.fetchall()
        aviso_ids= [aviso[0] for aviso in id_aviso]
        
        for aviso_id in aviso_ids:
            aviso= execute1(cur,Queryaviso, aviso_id)
            print(aviso)
            print("")
    else:
        print("Não há avisos por ler.")