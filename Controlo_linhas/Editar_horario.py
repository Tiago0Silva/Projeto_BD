from .Visualizar_horarios_linha import visualizar_horarios_linha
from .Alterar_hora import alterar_hora
def editar_horario(cur):
    visualizar_horarios_linha(cur)
    print("1- linha 1")
    print("2- linha 2")
    print("3- linha 3")
    linha= int(input("Escolha: "))
    
    alterar_hora(cur, linha)
    #alterar_freq(cur, linha)
            