from datetime import datetime, date
def gestao_precario_data(cur,linha, data):
    
    Query_data_precario="SELECT titulo, inicio_validade, fim_validade FROM precario WHERE id_linha= %s"
    Query_normal= "SELECT titulo FROM precario WHERE id_linha= %s AND inicio_validade IS NULL AND fim_validade IS NULL"
    cur.execute(Query_data_precario, (linha,))
    precarios = cur.fetchall()
    
    for titulo, inicio_validade, fim_validade in precarios:
        if inicio_validade is not None and fim_validade is not None:  
            if isinstance(inicio_validade, datetime):
                inicio_validade = inicio_validade.date()
            if isinstance(fim_validade, datetime):
                fim_validade = fim_validade.date()
            if inicio_validade <= data <= fim_validade:
                return titulo
            
    cur.execute(Query_normal, (linha,))
    result = cur.fetchone()
    return result[0]   