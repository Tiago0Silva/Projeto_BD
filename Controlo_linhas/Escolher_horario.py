from Controlo_horarios.gerar_horarios import gerar_horarios
def escolher_horario(conn, cur, linha_id):

    print("\nEscolha o par de horários a ativar para a Linha 3:")
    print("1 - Ativar os 2 primeiros horários")
    print("2 - Ativar os 2 últimos horários")
    escolha = int(input("Selecione: "))

    if escolha == 1:
        # Ativar os 2 primeiros (IDs 3 e 4 por exemplo)
        try:
            cur.execute("UPDATE linha_freq SET horario_impl = FALSE WHERE id_linha = 3")
            conn.commit()
            cur.execute("UPDATE linha_freq SET horario_impl = TRUE WHERE id IN (3, 4)")
            conn.commit()
            print("✔ Horários ativados.")
        except Exception as e:
            print(f"Erro: {e}")
            conn.rollback()
        
    elif escolha == 2:
        # Ativar os 2 últimos (IDs 5 e 6 por exemplo)
        try:
            cur.execute("UPDATE linha_freq SET horario_impl = FALSE WHERE id_linha = 3")
            conn.commit()
            cur.execute("UPDATE linha_freq SET horario_impl = TRUE WHERE id IN (5, 6)")
            conn.commit()
            print("✔ Horários ativados.")
        except Exception as e:
            print(f"Erro: {e}")
            conn.rollback()
        
    cur.execute("SELECT id FROM linha_freq WHERE id_linha = %s AND horario_impl = TRUE", (linha_id,))
    ids = [row[0] for row in cur.fetchall()]
    cur.execute("SELECT id FROM linha__trecho WHERE id_linha= %s", (linha_id,))
    linha_trecho_id= [row[0] for row in cur.fetchall()]  
    # Gerar os horários com base nesses dois IDs
    print(ids)
    for id_horario in ids:
        gerar_horarios(conn, cur, id_horario, linha_trecho_id)