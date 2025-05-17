def reembolsos_cancelamentos(conn, cur):
    try:
        # 1. Obter pedidos pendentes
        query_analise_pedido= "SELECT bp.estado_utilizacao, bp.data_viagem, pgbp.utilizador_id, pgbp.id_bilhete_passe, pgbp.id, pgbp.justificacao FROM bilhete_passe bp, pedido_gestao_bilhetes_passes pgbp WHERE tipo_pedido='Cancelamento' AND estado_aceitacao ='por avaliar' AND bp.id= pgbp.id_bilhete_passe"
        cur.execute(query_analise_pedido)
        resultados = cur.fetchall()

        if not resultados:
            print("Não há pedidos pendentes de avaliação.")
            return
        while True:
            print("\nPedidos pendentes:")
            print("estado_utilização | Data da viagem | Usuário ID | Bilhete ID | Pedido ID")
            print("-" * 70)
            for pedido in resultados:
                data = pedido[1].strftime('%Y-%m-%d %H:%M') if pedido[1] else 'Data inválida'
                print(f"{pedido[0]:<5} | {data:<20} | {pedido[2]:<9} | {pedido[3]:<9} | {pedido[4]:<9}")

            pedido_id = int(input("\nInsira o ID do pedido que deseja avaliar: "))
            #verificar se o id está na lista 
            break
            
        Query_detalhes= "SELECT bp.data_viagem, pgbp.id_bilhete_passe, pgbp.utilizador_id, pgbp.justificacao ,t.valor FROM transacao t,pedido_gestao_bilhetes_passes pgbp, bilhete_passe bp WHERE pgbp.id= %s AND bp.id= pgbp.id_bilhete_passe AND t.id= bp.transacao_id"
        cur.execute(Query_detalhes, (pedido_id,))
        detalhes = cur.fetchone()

        if not detalhes:
            raise ValueError("Pedido não encontrado ou já avaliado")

        print("\nDetalhes do Pedido:")
        print(f"Data da viagem: {detalhes[0]}")
        print(f"Bilhete ID: {detalhes[1]}")
        print(f"Usuário ID: {detalhes[2]}")
        print(f"\nJustificação:\n{detalhes[3]}")

        print("\nOpções:")
        print("1 - Aprovar com reembolso total (100%)")
        print("2 - Aprovar com reembolso parcial (70%)")
        print("3 - Recusar (sem reembolso)")
        
        opcao = input("Escolha uma opção (1-3): ")

        valor_reembolso = 0.0
        estado = ''

        if opcao == '1':
            estado = 'aceite'
            valor_reembolso = detalhes[4]
        elif opcao == '2':
            estado = 'aceite'
            valor_reembolso = detalhes[4] * 0.7 
        elif opcao == '3':
            estado = 'recusado'
            valor_reembolso = 0.0
        else:
            raise ValueError("Opção inválida")

        query_atualizar_pedido = "UPDATE pedido_gestao_bilhetes_passes SET estado_aceitacao = %s WHERE id = %s "
        cur.execute(query_atualizar_pedido, (estado, pedido_id))

        if valor_reembolso > 0:
            query_atualizar_saldo = "UPDATE utilizador SET saldo = saldo + %s WHERE id = %s"
            cur.execute(query_atualizar_saldo, (valor_reembolso, detalhes[2]))

        conn.commit()
        print(f"\nProcesso concluído com sucesso! Estado: {estado}")
        if valor_reembolso > 0:
            print(f"Valor reembolsado: {valor_reembolso:.2f}€")

    except ValueError as ve:
        conn.rollback()
        print(f"\nErro: {ve}")
    except Exception as e:
        conn.rollback()
        print(f"\nErro inesperado: {e}")
        import traceback
        traceback.print_exc()