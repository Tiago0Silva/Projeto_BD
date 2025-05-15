from .Saldo import Saldo
from Executes.Execute1 import execute1

def Fundos_Carteira(conn, cur, id):
    try:
        while True:
            print("\n1 - Adicionar fundos")
            print("2 - Voltar atrás")
            Salmenu = input("Escolha -> ")

            if Salmenu == '1':
                try:
                    valor = float(input("Digite o valor a adicionar: "))
                    if valor <= 0:
                        print("O valor deve ser maior que zero.")
                        continue

                    AdFundos = "UPDATE utilizador SET saldo = saldo + %s WHERE id = %s"
                    cur.execute(AdFundos, (valor, id))
                    conn.commit()

                    QuerySal = "SELECT saldo FROM utilizador WHERE id = %s"
                    novo_saldo = execute1(cur, QuerySal, id)
                    print("Novo saldo: ", novo_saldo)

                except ValueError:
                    print("Por favor, insira um valor numérico válido.")
                except Exception as e:
                    conn.rollback()
                    print("Erro ao adicionar fundos:", e)

            elif Salmenu == '2':
                print("A voltar ao menu anterior.")
                break

            else:
                print("Opção inválida, tente novamente.")

    except Exception as e:
        print("Erro geral no menu de fundos:", e)
