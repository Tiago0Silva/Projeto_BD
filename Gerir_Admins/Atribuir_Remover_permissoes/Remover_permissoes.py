from  Controlo_linhas.Visualizar_tabela import visualizar_tabela
def remover_permissoes(conn, cur):
    Query_Admins= "SELECT email, id FROM administrador WHERE super_admin= FALSE"
    cur.execute(Query_Admins)
    resultados= cur.fetchall()
    visualizar_tabela(cur, [resultados])
    id = input("Insira o ID do admin que quer retirar a permissão: ")
    Query_eliminar_admin = "DELETE FROM administrador WHERE id = %s AND super_admin = FALSE"
    cur.execute(Query_eliminar_admin, (id,))
                
    if cur.rowcount == 0:
        print("ID inválido ou o admin é um super_admin (não pode ser removido).")
    else:
        print("Permissões eliminadas com sucesso.")
                
    conn.commit()