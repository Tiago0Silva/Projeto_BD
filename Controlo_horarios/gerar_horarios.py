def gerar_horarios(cur, var1, var2, var3, var4, var5, var6):
    #gera horarios para o dia de hoje
    QueryViagens= "INSERT INTO  viagem (hora_inicio, hora_fim, lotacao_max, linha_freq_id, linha__trecho_id_linha, linha__trecho_sentido) VALUES (%s, %s, %s, %s, %s, %s)"
    cur.execute(QueryViagens, (var1, var2, var3, var4, var5, var6))

    #WHERE linha_freq_id = 1, linha__trecho_id_linha, linha__trecho_sentido = 'ida'