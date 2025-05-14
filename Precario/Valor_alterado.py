from Executes.Execute1 import execute1
from Controlo_linhas.Visualizar_tabela import visualizar_tabela
def valor_alterado(cur, linha, categoria):
    if categoria == 1:
        cat= 'viagem_unica'
    if categoria == 2:
        cat= 'diario'
    if categoria == 3:
        cat='passe_mensal'
    if categoria == 4:
        cat='passe_estudante'
    if categoria == 5:
        cat='passe_senior'
    Query_valor_antigo= f"SELECT {cat} FROM precario WHERE id_linha = %s"
    resposta= execute1(cur, Query_valor_antigo, linha)
    print(f"Valor atual de {cat}: {resposta}")
    novo_valor= float(input("Seleciona o volor novo: "))
    Query_alterar_valor = f"UPDATE precario SET {cat} = %s WHERE id_linha = %s"
    cur.execute(Query_alterar_valor, (novo_valor, linha))
    print("Alteração bem sucedida!")