def visualizar_tabela(cur, resultados):

    colunas = [desc[0] for desc in cur.description]

    print("\t".join(colunas))
    print("-" * 80)

    for linha in resultados:
        print("\t".join(str(campo) for campo in linha))