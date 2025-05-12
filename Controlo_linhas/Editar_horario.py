from .Visualizar_horarios_linha import visualizar_horarios_linha
from .Alterar_hora import alterar_hora
from Controlo_horarios.gerar_horarios import gerar_horarios

def editar_horario(conn, cur):
    visualizar_horarios_linha(cur)
    print("Que horário pretende editar?")
    print("1- linha 1")
    print("2- linha 2")
    print("3- linha 3")
    linha= int(input("Escolha: "))
    while True:
        if linha == 1:
            alterar_hora(cur, linha)
            #alterar_freq(cur, linha)
            cur.execute("SELECT id FROM linha__trecho WHERE id_linha= %s", linha)
            ids= [row[0] for row in cur.fetchall()]
            for linha_trecho_id in ids:
                gerar_horarios(conn, cur, linha, linha_trecho_id)
        if linha == 2:
            alterar_hora(cur, linha)
            #alterar_freq(cur, linha)
            cur.execute("SELECT id FROM linha__trecho WHERE id_linha= %s", linha)
            ids= [row[0] for row in cur.fetchall()]
            for linha_trecho_id in ids:
                gerar_horarios(conn, cur, linha, linha_trecho_id)
        if linha == 3:
            alterar_hora(cur, linha)
            #alterar_freq(cur, linha)
            cur.execute("SELECT id FROM linha__trecho WHERE id_linha= %s", linha)
            ids= [row[0] for row in cur.fetchall()]
            for linha_trecho_id in ids:
                gerar_horarios(conn, cur, linha, linha_trecho_id)  
        if linha == 0:
            break
        