from Gestao_bilhetes_cliente.Cancelamento import cancelamento
def gerir_bilhetes(conn, cur, id):
    
    Query_ver_tudo=  "SELECT v.hora_inicio, v.hora_fim, lt.sentido, bp.data_viagem, lt.loc_partida, lt.loc_chegada, bp.estado_utilizacao, bp.id FROM viagem v, linha__trecho lt, bilhete_passe bp, transacao t, bilhete_passe_viagem bpv,linha_freq lf WHERE t.utilizador_id= %s AND bp.transacao_id= t.id AND bpv.bilhete_passe_id=bp.id AND bpv.viagem_id=v.id AND v.linha__trecho_id=lt.id AND v.linha_freq_id=lf.id ORDER BY bp.data_viagem, v.hora_inicio, bp.id"
    
    cur.execute(Query_ver_tudo, (id,))
    resultados = cur.fetchall()
    
    if not resultados:
        print("Não foram encontrados bilhetes para este utilizador.")
        return
    
    ids_validos = [row[7] for row in resultados]
    
    print(f"{'Hora Início':<12} | {'Hora Fim':<12} | {'Sentido':<8} | {'Data Viagem':<12} | {'Partida':<15} | {'Chegada':<15} | {'Estado':<20} | {'ID bilhete'}")
    print("-" * 115)
    
    for row in resultados:
        hora_inicio, hora_fim, sentido, data_viagem, loc_partida, loc_chegada, estado, id = row
        print(f"{str(hora_inicio):<12} | {str(hora_fim):<12} | {str(sentido):<8} | {str(data_viagem):<12} | {loc_partida:<15} | {loc_chegada:<15} | {estado:<20} | {id}")
        
    print("1- Sim")
    print("2- Não")
    mudar_estado= int(input("Pretende mudar o estado de algum bilhete ou passe?"))
    
    if mudar_estado == 1:
        try:
            bilhete_id = int(input("Digite o ID do bilhete: "))
            
            if bilhete_id not in ids_validos:
                print("ID inválido. Tente novamente.")
                return
            
            cur.execute("SELECT estado_utilizacao FROM bilhete_passe WHERE id = %s", (bilhete_id,))
            estado_atual = cur.fetchone()[0]
            
            if estado_atual == 'USADO':
                print("Este bilhete já foi utilizado e não pode ser alterado.")
                return
            
            print("\nOpções de estado:")
            print("1 - CANCELAR")
            print("2 - USADO")
            print("3 - Voltar")
            
            opcao_estado = input("Escolha o novo estado (1-3): ")
            
            if opcao_estado == '1':
                novo_estado = 'CANCELADO'
                cancelamento(conn, cur,id, bilhete_id)
                
            elif opcao_estado == '2':
                novo_estado = 'USADO'
            elif opcao_estado == '3':
                return
            else:
                print("Opção inválida.")
                return
            
            try:
                cur.execute("UPDATE bilhete_passe SET estado_utilizacao = %s WHERE id = %s", 
                          (novo_estado, bilhete_id))
                conn.commit()
                print(f"Estado do bilhete {bilhete_id} atualizado para {novo_estado} com sucesso!")
            except Exception as e:
                conn.rollback()
                print(f"Erro ao atualizar o bilhete: {e}")
                
        except ValueError:
            print("ID inválido. Deve digitar um número.")
    elif mudar_estado == 2:
        return
    else:
        print("Opção inválida.")