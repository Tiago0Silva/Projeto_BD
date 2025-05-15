from Controlo_linhas.Visualizar_tabela import visualizar_tabela

def remover_permissoes(conn, cur):
    try:
        Query_Admins = "SELECT email, id FROM administrador WHERE super_admin = FALSE"
        cur.execute(Query_Admins)
        resultados = cur.fetchall()

        if not resultados:
            print("Não há administradores removíveis.")
            return

        visualizar_tabela(cur, resultados)

        id_input = input("Insira o ID do admin que quer retirar a permissão: ")

        try:
            id = int(id_input)
        except ValueError:
            print("ID inválido. Deve ser um número inteiro.")
            return

        Query_eliminar_admin = "DELETE FROM administrador WHERE id = %s AND super_admin = FALSE"
        cur.execute(Query_eliminar_admin, (id,))

        if cur.rowcount == 0:
            print("ID inválido ou o admin é um super_admin (não pode ser removido).")
        else:
            conn.commit()
            print("Permissões eliminadas com sucesso.")

    except Exception as e:
        conn.rollback()
        print("Erro ao remover permissões:", e)
