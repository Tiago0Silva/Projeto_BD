from .Visualizar_horarios_linha import visualizar_horarios_linha
from .Alterar_horario_ativo import alterar_horario_ativo
from .Editar_horario import editar_horario
def controlo_linha(conn, cur):
    #ver todos os horários de linha
    try:
        while True:
            visualizar_horarios_linha(cur)
            print("1- Alterar horário ativo")
            print("2- Editar Horario Ativo")
            print("0- Sair")
            op= int(input("Escolha: "))
            if op == 1:
                alterar_horario_ativo(conn, cur)
            if op == 2:
                editar_horario(conn, cur)
            if op == 0:
                break
    except Exception as e:
            print("Ocorreu um erro: ", e)
