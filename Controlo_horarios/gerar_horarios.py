from Controlo_linhas.Visualizar_tabela import visualizar_tabela
from datetime import timedelta

def gerar_horarios(conn, cur, id, linha_trecho_id):
    cur.execute("SELECT abertura, fecho, frequencia, id_linha FROM linha_freq WHERE id = %s", (id,))
    resultado = cur.fetchone()
    
    if resultado is None:
        print(f"❌ Nenhum resultado encontrado para id {id}")
        return

    visualizar_tabela(cur, [resultado])  # resultado é uma tupla, colocamos entre [] para simular lista de linhas

    abertura, fecho, frequencia, id_linha = resultado
    
    # Elimina viagens anteriores
    cur.execute("DELETE FROM viagem WHERE linha_freq_id = %s", (id,))
    conn.commit()

    # Prepara viagens novas
    viagens = []
    atual = abertura
    while atual + timedelta(minutes=frequencia) <= fecho:
        fim = atual + timedelta(minutes=frequencia)
        viagens.append((partida := atual, chegada := fim))
        atual = fim

    # Insere viagens
    for partida, chegada in viagens:
        for trecho_id in linha_trecho_id:  # se linha_trecho_id for uma lista de IDs
            cur.execute(
                "INSERT INTO viagem (hora_inicio, hora_fim, linha_freq_id, linha__trecho_id) VALUES (%s, %s, %s, %s)",
                (partida, chegada, id, trecho_id)
            )
    conn.commit()