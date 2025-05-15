from Controlo_linhas.Visualizar_tabela import visualizar_tabela
from datetime import timedelta

def gerar_horarios(conn, cur, id_linha, linha_trecho_id):
    try:
        cur.execute("SELECT id, abertura, fecho, frequencia FROM linha_freq WHERE id_linha = %s", (id_linha,))
        resultado = cur.fetchone()
        if resultado is None:
            print(f"Nenhuma frequência encontrada para a linha com id {id_linha}.")
            return

        cur.execute("SELECT sentido FROM linha__trecho WHERE id = %s", (linha_trecho_id,))
        sentido = cur.fetchone()
        if sentido is None:
            print(f"Trecho com id {linha_trecho_id} não encontrado.")
            return

        visualizar_tabela(cur, [resultado])

        id_freq, abertura, fecho, frequencia = resultado

        cur.execute("DELETE FROM viagem WHERE linha__trecho_id = %s AND linha_freq_id = %s", (linha_trecho_id, id_freq))

        viagens = []
        atual = abertura

        if sentido[0] == 'volta':
            atual = abertura + timedelta(minutes=frequencia)

        while atual + timedelta(minutes=frequencia) <= fecho:
            fim = atual + timedelta(minutes=frequencia)
            viagens.append((atual, fim))
            atual = fim + timedelta(minutes=frequencia)

        print("Viagens a inserir:")
        for partida, chegada in viagens:
            print(f"  {partida} -> {chegada}")

        for partida, chegada in viagens:
            cur.execute(
                "INSERT INTO viagem (hora_inicio, hora_fim, linha_freq_id, linha__trecho_id) VALUES (%s, %s, %s, %s)",
                (partida, chegada, id_freq, linha_trecho_id)
            )

        conn.commit()
        print("Viagens geradas e inseridas com sucesso.")

    except Exception as e:
        conn.rollback()
        print("Erro ao gerar horários:", e)
