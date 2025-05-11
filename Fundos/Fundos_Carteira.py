from .Saldo import Saldo
from Executes.Execute1 import execute1
def Fundos_Carteira(cur, id):
    Saldo(cur, id)
    try:
        Salmenu=0
        while True:
            print("1- Adicionar fundos")
            print("2- Voltar ao menu principal")
            Salmenu= input("Escolha -> ")
            
            if Salmenu == '1':
                try:
                    valor = float(input("Digite o valor a adicionar: "))
                    if valor <= 0:
                        print("O valor deve ser maior que zero.")
                        continue
                    
                    AdFundos = "UPDATE utilizador SET saldo = saldo + %s WHERE id = %s"
                    cur.execute(AdFundos, (valor, id))
                    cur.connection.commit()
                    QuerySal = "SELECT saldo FROM utilizador WHERE id= %s"
                    novo_saldo = execute1(cur, QuerySal, id)
                    print("Novo saldo: ", novo_saldo)
                except ValueError:
                    print("Por favor, insira um valor numérico válido.")
                
            elif Salmenu == '2':
                break
            else:
                print("Opção inválida, tente novamente.")
    except Exception as e:
        print("Ocorreu um erro: ", e)