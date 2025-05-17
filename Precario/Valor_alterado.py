from Executes.Execute1 import execute1
from Controlo_linhas.Visualizar_tabela import visualizar_tabela

def valor_alterado(conn, cur, linha, categoria):
    try:
        cur.execute("BEGIN")
        
        categorias = {
            1: 'viagem_unica',
            2: 'diario',
            3: 'passe_mensal',
            4: 'passe_estudante',
            5: 'passe_senior'
        }
        cat = categorias.get(categoria)
        
        if not cat:
            raise ValueError("Categoria inválida")

        Query_valor_antigo = f"""
            SELECT {cat} 
            FROM precario 
            WHERE id_linha = %s
            FOR UPDATE  -- Bloqueia a linha durante a transação
        """
        resposta = execute1(cur, Query_valor_antigo, linha)
        
        if not resposta:
            conn.rollback()
            print("Linha não encontrada no precário!")
            return

        print(f"\nValor atual de {cat}: {resposta[0]}")
        novo_valor = float(input("Novo valor: "))

        Query_alterar_valor = f"""
            UPDATE precario 
            SET {cat} = %s 
            WHERE id_linha = %s
        """
        cur.execute(Query_alterar_valor, (novo_valor, linha))

        visualizar_tabela(cur, "precario", f"id_linha = {linha}")
        
        conn.commit()
        print("\n✅ Alteração concluída com sucesso!")

    except ValueError as e:
        conn.rollback()
        print(f"❌ Erro: {str(e)}")
    except Exception as e:
        conn.rollback()
        print(f"❌ Erro inesperado: {str(e)}")