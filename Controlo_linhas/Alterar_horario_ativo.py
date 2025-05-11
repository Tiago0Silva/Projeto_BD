from .Visualizar_tabela import visualizar_tabela
from .Escolher_horario import escolher_horario
from .Visualizar_horarios_linha import visualizar_horarios_linha
def alterar_horario_ativo(cur):
    Query_linha1 = "SELECT abertura, fecho, frequencia, id_linha, horario_impl FROM linha_freq WHERE id_linha= 1"
    Query_linha2 = "SELECT abertura, fecho, frequencia, id_linha, horario_impl FROM linha_freq WHERE id_linha= 2"
    Query_linha3 = "SELECT abertura, fecho, frequencia, id_linha, horario_impl FROM linha_freq WHERE id_linha= 3"
    try:
        while True:
            print("1- linha1")
            print("2- linha2")
            print("3- linha3")
            print("0- Sair")
            linha= int(input("Selecione:"))
            
            if linha == 1:
                cur.execute(Query_linha1)
                resultados1= cur.fetchall()
                visualizar_tabela(cur, resultados1)
                #colocar aqui a opção de editar
            
            if linha == 2:
                cur.execute(Query_linha2)
                resultados2= cur.fetchall()
                visualizar_tabela(cur, resultados2)
                #colocar aqui a opção de editar
            
            if linha == 3:
                cur.execute(Query_linha3)
                resultados3= cur.fetchall()
                visualizar_tabela(cur, resultados3)
                escolher_horario(cur)
                visualizar_horarios_linha(cur)
            if linha == 0:
                break
            
    except Exception as e:
        print("Ocorreu um erro: ", e)