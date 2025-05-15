def horarios_cliente(cur, linha):
    query = "SELECT v.id, v.hora_inicio, v.hora_fim, lt.loc_partida, lt.loc_chegada, lt.sentido FROM linha__trecho AS lt JOIN viagem AS v ON lt.id = v.linha__trecho_id WHERE lt.id_linha = %s ORDER BY v.hora_inicio"

    try:
        cur.execute(query, (linha,))    
        resultados = cur.fetchall()
            
        print(f"{'ID':<10} {'Hora Início':<20} {'Hora Fim':<20} {'Partida':<15} {'Chegada':<15} {'Sentido':<10}")
        print("-" * 100)
        for id_viagem, hora_inicio, hora_fim, partida, chegada, sentido in resultados:
            print(f"{id_viagem:<5} {str(hora_inicio):<20} {str(hora_fim):<20} {partida:<15} {chegada:<15} {sentido:<10}")
    except Exception as e:
        print("Ocorreu um erro: ", e)
            