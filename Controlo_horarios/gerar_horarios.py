from Controlo_linhas.Visualizar_tabela import visualizar_tabela
from datetime import timedelta

def gerar_horarios(conn, cur, id_linha, linha_trecho_id):
    
    cur.execute("SELECT id, abertura, fecho, frequencia FROM linha_freq WHERE id_linha = %s", (id_linha,))
    resultado = cur.fetchone()
    cur.execute("SELECT sentido FROM linha__trecho WHERE id= %s", (linha_trecho_id,))
    sentido= cur.fetchone()
    if resultado is None:
        print(f"❌ Nenhum resultado encontrado para id {id}")
        return

    visualizar_tabela(cur, [resultado])  # resultado é uma tupla, colocamos entre [] para simular lista de linhas

    id_freq, abertura, fecho, frequencia = resultado
    visualizar_tabela(cur, [resultado[1:]])
     
    # Elimina viagens anteriores
    cur.execute("DELETE FROM viagem WHERE linha__trecho_id= %s AND linha_freq_id = %s", (linha_trecho_id, id_freq,))
    conn.commit() 

    # Prepara viagens novas
    viagens = []
    atual = abertura
    if sentido[0] == 'volta':
        atual= abertura + timedelta(minutes=frequencia)
        
    while atual + timedelta(minutes=frequencia) <= fecho:
        fim = atual + timedelta(minutes=frequencia)
        viagens.append((partida := atual, chegada := fim))
        atual = fim + timedelta(minutes=frequencia)
    print("Viagens a inserir:")
    for partida, chegada in viagens:
        print(f"  {partida} -> {chegada}")

    # Insere viagens
    for partida, chegada in viagens:
        print(f"Inserir: partida={partida}, chegada={chegada}, id_freq={id_freq}, trecho={linha_trecho_id}")
        cur.execute("INSERT INTO viagem (hora_inicio, hora_fim, linha_freq_id, linha__trecho_id) VALUES (%s, %s, %s, %s)",        (partida, chegada, id_freq, linha_trecho_id))
    conn.commit()