from  Controlo_linhas.Visualizar_tabela import visualizar_tabela
from Gerir_Admins.Atribuir_Remover_permissoes.Remover_permissoes import remover_permissoes
from Gerir_Admins.Atribuir_Remover_permissoes.Atribuir_permissoes import atribuicao_permissoes
def gerir_admins(conn, cur):
    while True:
        print("1- Remover permissões")
        print("2- Atribuição permissão")
        print("0- Voltar ao menu principal")
        selecao = int(input("Escolha: "))
        if selecao == 1:
            remover_permissoes(conn, cur)
        if selecao == 2:
            atribuicao_permissoes(conn, cur)
        if selecao == 0:
            return