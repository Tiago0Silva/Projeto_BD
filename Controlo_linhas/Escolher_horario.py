def escolher_horario(cur):

    print("\nEscolha o par de horários a ativar para a Linha 3:")
    print("1 - Ativar os 2 primeiros horários")
    print("2 - Ativar os 2 últimos horários")
    escolha = int(input("Selecione: "))

    if escolha == 1:
        # Ativar os 2 primeiros (IDs 3 e 4 por exemplo)
        cur.execute("UPDATE linha_freq SET horario_impl = FALSE WHERE id_linha = 3")
        cur.execute("UPDATE linha_freq SET horario_impl = TRUE WHERE id IN (3, 4)")
        print("✔ Horários 3 e 4 ativados.")
        
    elif escolha == 2:
        # Ativar os 2 últimos (IDs 5 e 6 por exemplo)
        cur.execute("UPDATE linha_freq SET horario_impl = FALSE WHERE id_linha = 3")
        cur.execute("UPDATE linha_freq SET horario_impl = TRUE WHERE id IN (5, 6)")
        print("✔ Horários 5 e 6 ativados.")
