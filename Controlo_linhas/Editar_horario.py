from .Visualizar_horarios_linha import visualizar_horarios_linha
from .Alterar_hora import alterar_hora
from Controlo_horarios.gerar_horarios import gerar_horarios

def editar_horario(conn, cur):
    while True:
        visualizar_horarios_linha(cur)
        print("Que horário pretende editar?")
        print("1- linha 1")
        print("2- linha 2")
        print("3- linha 3")
        print("0- Sair")
        linha = int(input("Escolha: "))

        if linha == 0:
            break

        if linha in [1, 2, 3]:
            alterar_hora(conn, cur, linha)
            cur.execute("SELECT id FROM linha__trecho WHERE id_linha= %s", (linha,))
            ids = [row[0] for row in cur.fetchall()]
            for linha_trecho_id in ids:
                gerar_horarios(conn, cur, linha, linha_trecho_id)
        else:
            print("❌ Opção inválida.")
