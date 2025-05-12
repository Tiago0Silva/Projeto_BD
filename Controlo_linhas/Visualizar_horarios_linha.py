from .Visualizar_tabela import visualizar_tabela

def visualizar_horarios_linha(cur):
    Query_linhas = "SELECT abertura, fecho, frequencia, id_linha, horario_impl FROM linha_freq WHERE horario_impl= TRUE ORDER BY id_linha"
    cur.execute(Query_linhas)
    resultados = cur.fetchall()
    visualizar_tabela(cur, resultados)