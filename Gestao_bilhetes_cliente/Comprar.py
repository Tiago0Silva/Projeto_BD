from datetime import datetime, date
from .Transacao import transacao
from .horarios_cliente import horarios_cliente

def comprar(conn, cur, titulo, id_utilizador, linha):
    try:
        Query_insert_bilhete = "INSERT INTO bilhete_passe (categoria, data_viagem, transacao_id) VALUES (%s, %s, %s) RETURNING id"
        Query_insert_relacao = "INSERT INTO bilhete_passe_viagem (bilhete_passe_id, viagem_id) VALUES (%s, %s)"

        Query_precario = "SELECT viagem_unica, diario, passe_mensal, passe_estudante, passe_senior FROM precario WHERE id_linha = %s AND titulo = %s"
        cur.execute(Query_precario, (linha, titulo,))
        categoria = cur.fetchone()

        print("1- Viagem única | 2- Diário | 3- Passe Mensal | 4- Passe Estudante | 5- Passe Sénior")
        print(f"{categoria[0]:<15} | {categoria[1]:<15} | {categoria[2]:<15} | {categoria[3]:<15} | {categoria[4]:<15}")

        cat = None
        data_viagem = None
        id_viagem = None

        while True:
            try:
                categoria_num = int(input("Insira a categoria de viagem que quer: "))
            except ValueError:
                print("Insira um número válido.")
                continue

            if categoria_num == 1:
                cat = 'viagem_unica'
                horarios_cliente(cur, linha)
                while True:
                    try:
                        id_viagem = int(input("Insira o ID da viagem que pretende: "))
                        data_str = input("Insira a data da viagem (formato: AAAA-MM-DD): ")
                        data_viagem = datetime.strptime(data_str, "%Y-%m-%d").date()
                        if data_viagem < date.today():
                            print("A data não pode ser no passado.")
                            continue
                        break
                    except ValueError:
                        print("Formato de data inválido. Use AAAA-MM-DD.")
                break
            elif categoria_num == 2:
                cat = 'diario'
                while True:
                    try:
                        data_str = input("Insira a data do passe diário (formato: AAAA-MM-DD): ")
                        data_viagem = datetime.strptime(data_str, "%Y-%m-%d").date()
                        if data_viagem < date.today():
                            print("A data não pode ser no passado.")
                            continue
                        break
                    except ValueError:
                        print("Formato de data inválido. Use AAAA-MM-DD.")
                break
            elif categoria_num == 3:
                cat = 'passe_mensal'
                break
            elif categoria_num == 4:
                cat = 'passe_estudante'
                break
            elif categoria_num == 5:
                cat = 'passe_senior'
                break
            else:
                print("Categoria inválida. Escolha um número entre 1 e 5.")

        validacao = input("Prima 1 para validar a compra: ")
        if validacao != '1':
            print("Compra cancelada.")
            return

        tipo = 'Compra'
        id_transacao = transacao(conn, cur, cat, titulo, tipo, id_utilizador, linha)
        if id_transacao is None:
            print("Transação falhou. Compra cancelada.")
            return

        cur.execute(Query_insert_bilhete, (cat, data_viagem, id_transacao))
        id_bilhete = cur.fetchone()[0]

        # Só insere na tabela de relação se for uma viagem única
        if cat == 'viagem_unica' and id_viagem is not None:
            cur.execute(Query_insert_relacao, (id_bilhete, id_viagem))

        conn.commit()
        print("Compra efetuada com sucesso.")

    except Exception as e:
        conn.rollback()
        print("Erro ao finalizar compra:", e)
