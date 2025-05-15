from Controlo_linhas.Visualizar_tabela import visualizar_tabela

def atribuicao_permissoes(conn, cur):
    Query_utilizadores = "SELECT email, nome, id FROM utilizador"
    cur.execute(Query_utilizadores)
    resultados = cur.fetchall()
    visualizar_tabela(cur, resultados)

    while True:
        try:
            print("\nSelecione o ID do utilizador que quer promover a administrador:")
            selecao = int(input("Escolha: "))

            ids_disponiveis = [r[2] for r in resultados]
            if selecao not in ids_disponiveis:
                print("ID inválido. Tente novamente.")
                continue

            email = next(r[0] for r in resultados if r[2] == selecao)

            cur.execute("SELECT email FROM administrador WHERE email = %s", (email,))
            if cur.fetchone() is not None:
                print("Este utilizador já é administrador.")
                return

            while True:
                password = input("Insira a password para o novo administrador: ")
                if not password or len(password) < 6:
                    print("Mínimo de 6 caracteres.")
                else:
                    break

            try:
                cur.execute(
                    "INSERT INTO administrador (email, password, super_admin) VALUES (%s, %s, FALSE)",
                    (email, password)
                )
                conn.commit()
                print("Utilizador promovido a administrador com sucesso.")
                break
            except Exception as e:
                conn.rollback()
                print("Erro ao inserir administrador:", e)
                break

        except ValueError:
            print("Insira um número válido.")
        except Exception as e:
            print("Erro inesperado:", e)
            break
