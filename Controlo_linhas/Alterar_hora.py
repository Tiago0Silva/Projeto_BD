from .Visualizar_tabela import visualizar_tabela

def alterar_hora(cur, linha):
    Query_linhas = "SELECT abertura, fecho, frequencia, horario_impl FROM linha_freq WHERE id_linha = %s AND horario_impl = TRUE"
    cur.execute(Query_linhas, (linha,))
    resultados = cur.fetchall()
    visualizar_tabela(cur, resultados)

    try:
        while True:
            print("\n1 - Alterar hora de entrada")
            print("2 - Alterar hora de saída")
            print("0 - Sair")
            alt = int(input("Escolha: "))

            if alt == 1:
                nova_abertura = input("Insira a nova hora de entrada (formato HH:MM): ")
                nova_abertura_completa = f"2000-01-01 {nova_abertura}:00"
                cur.execute("""
                    UPDATE linha_freq
                    SET abertura = %s
                    WHERE id_linha = %s AND horario_impl = TRUE
                """, (nova_abertura_completa, linha))
                print("Hora de entrada atualizada com sucesso.")

            elif alt == 2:
                novo_fecho = input("Insira a nova hora de saída (formato HH:MM): ")
                novo_fecho_completo = f"2000-01-01 {novo_fecho}:00"
                cur.execute("""
                    UPDATE linha_freq
                    SET fecho = %s
                    WHERE id_linha = %s AND horario_impl = TRUE
                """, (novo_fecho_completo, linha))
                print("Hora de saída atualizada com sucesso.")

            elif alt == 0:
                print("A sair da edição de horários.")
                break

    except Exception as e:
        print("Ocorreu um erro: ", e)

    except Exception as e:
        print("Ocorreu um erro: ", e)