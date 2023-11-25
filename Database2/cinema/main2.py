import psycopg2

def conexao_banco():
    mydb = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="1234",
        database="bd2")
    return mydb

def menu():
    print('1 -- Consulta sessões')
    print('2 -- Vendas de ingresso')
    print('3 -- Consultar sessao especifica')
    print('4 -- Consultar lista de espera')
    print('-' * 40)

    opcao = int(input('Digite a opção desejada: '))
    return opcao

consulta = conexao_banco()

while True:
    opcao = menu()

    if opcao == 1:
        cursor = consulta.cursor()
        pesquisar = ("SELECT * FROM consulta_sessoes()")
        cursor.execute(pesquisar)
        resultado = cursor.fetchall()
        
        print('\nSessões: ')
        for i in resultado:
            print(f"Número Sala: {i[0]}, Nome Filme: {i[1]}, Data Sessão: {i[2]}, Horário Sessão: {i[3]}, Poltrona Venda: {i[4]}")
        print('-' * 80 + '\n')

    elif opcao == 2:
            cod_sessao = int(input("Digite o código da sessão: "))
            cod_cliente = int(input("Digite o código do cliente: "))
            num_poltrona = int(input("Digite o número da poltrona: "))

            cursor = consulta.cursor()
            venda = ("SELECT venda_ingressos(%s, %s, %s)")
            cursor.execute(venda, (cod_sessao, cod_cliente, num_poltrona))
            resultado = cursor.fetchone()

            print('\nVenda de ingressos: ')
            print(resultado)
            print('-' * 80 + '\n')
            consulta.commit()


    elif opcao == 3:
        cursor = consulta.cursor()
        numero_sessao = int(input("Digite o numero da sessao: "))

        pesquisar = ("SELECT * FROM consulta_sessao_especificas(%s)")
        cursor.execute(pesquisar, (numero_sessao,))

        resultados = cursor.fetchall()

        if resultados:
            print("\nSeção especifica:")
            for resultado in resultados:
                numero_sala, nome_filme, data_sessao, horario_sessao, poltrona_venda = resultado
                print(f"Numero Sala: {numero_sala}| Nome Filme: {nome_filme}| Data Sessao: {data_sessao}| Horario Sessao: {horario_sessao}| Poltrona Venda: {poltrona_venda}")
        else:
            print("Nenhum resultado encontrado para a sessao especificada.")
        print('-' * 90 + '\n')
            
    elif opcao == 4:
        
        cursor = consulta.cursor()
        pesquisar = ("SELECT * FROM lista_esperas()")
        cursor.execute(pesquisar)
        resultado = cursor.fetchall()

        print('\nLista de Espera: ')
        for i in resultado:
            print(f"Codigo sessão: {i[0]}| Codigo cliente: {i[1]}| Poltrona: {i[2]}| Data de registro: {i[3]}")
        print('-' * 95 + '\n')


cursor.close()
consulta.close()
