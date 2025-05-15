from .Visualizar_tabela import visualizar_tabela

def alterar_hora(conn, cur, linha):
    try:
        Query_linhas = "SELECT abertura, fecho, frequencia, horario_impl FROM linha_freq WHERE id_linha = %s AND horario_impl = TRUE"
        cur.execute(Query_linhas, (linha,))
        resultados = cur.fetchall()

        if not resultados:
            print(f"Nenhum horário encontrado com `horario_impl = TRUE` para a linha {linha}.")
            return

        visualizar_tabela(cur, resultados)

        while True:
            print("\n1 - Alterar hora de entrada")
            print("2 - Alterar hora de saída")
            print("0 - Sair")
            try:
                alt = int(input("Escolha: "))
            except ValueError:
                print("Opção inválida. Introduza um número.")
                continue

            if alt == 1:
                nova_abertura = input("Insira a nova hora de entrada (formato HH:MM): ")
                nova_abertura_completa = f"2000-01-01 {nova_abertura}:00"
                try:
                    cur.execute("""
                        UPDATE linha_freq
                        SET abertura = %s
                        WHERE id_linha = %s AND horario_impl = TRUE
                    """, (nova_abertura_completa, linha))
                    conn.commit()
                    print("Hora de entrada atualizada com sucesso.")
                except Exception as e:
                    conn.rollback()
                    print("Erro ao atualizar hora de entrada:", e)

            elif alt == 2:
                novo_fecho = input("Insira a nova hora de saída (formato HH:MM): ")
                novo_fecho_completo = f"2000-01-01 {novo_fecho}:00"
                try:
                    cur.execute("""
                        UPDATE linha_freq
                        SET fecho = %s
                        WHERE id_linha = %s AND horario_impl = TRUE
                    """, (novo_fecho_completo, linha))
                    conn.commit()
                    print("Hora de saída atualizada com sucesso.")
                except Exception as e:
                    conn.rollback()
                    print("Erro ao atualizar hora de saída:", e)

            elif alt == 0:
                print("A sair da edição de horários.")
                break
            else:
                print("Opção inválida. Tente novamente.")
    except Exception as e:
        print("Erro geral ao alterar horários:", e)