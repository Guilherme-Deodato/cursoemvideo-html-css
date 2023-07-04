# Início do programa 
 
listaPecas = [] 
codigoPeca = 0 
 
# Função que cadastra peças no sistema. 
def  cadastrarPeca(codigo):
    print('Você selecionou a opção de cadastrar Peça') 
    print('Código da Peça {}'.format(codigo)) 
    nomePeca = input('Por favor entre com o NOME da peça:') 
    fabricantePeca = input('Por favor entre com o FABRICANTE da peça:') 
    valorPeca = int(input('Por favor entre com o VALOR(R$) da peça:')) 
    dicionarioPeca = {'codigo': codigo, 
                      'nome': nomePeca, 
                      'fabricante': fabricantePeca, 
                      'valor': valorPeca} 
    listaPecas.append(dicionarioPeca.copy()) 
 
 
# Função que consulta as peças cadastradas no sistema. 
def consultarPeca(): 
    while True: 
        try: 
            print('Você selecionou a opção de Consultar Peça') 
            opConsultar = int(input('Escolha a opção desejada:\n' 
                                    '1-Consultar Todas as Peças\n' 
                                    '2-Consultar Peças por Código\n' 
                                    '3-Consultar Peças por Fabricante\n' 
                                    '4-Retornar\n' 
                                    '>>')) 
            if opConsultar == 1: 
                print('Você selecionou a opção 1-Consultar Todas as Peças selecionada') 
                for pecas in listaPecas: 
                    for key, value in pecas.items(): 
                        print('{} : {}'.format(key, value)) 
            elif opConsultar == 2: 
                print('Você selecionou a opção 2-Consultar Peças por Código') 
                entrada = int(input('Digite o CÓDIGO da Peça:')) 
                for pecas in listaPecas: 
                    if (pecas['codigo'] == entrada): 
                        for key, value in pecas.items(): 
                            print('{} : {}'.format(key, value)) 
            elif opConsultar == 3: 
                print('Você selecionou a opção 3-Consultar peça por Fabricante') 
                entrada = input('Digite a turma desejada:') 
                for pecas in listaPecas: 
                    if (pecas['fabricante'] == entrada): 
                        for key, value in pecas.items(): 
                            print('{} : {}'.format(key, value)) 
            elif opConsultar == 4: 
                break 
            else: 
                print('Digite uma opção que esteja no menu') 
                continue 
        except ValueError: 
            print('Insira apenas valores numéricos inteiros') 
 
 
# Função que remove peças cadastradas no sistema. 
def removerPeca(): 
    print('Você selecionou a opção de Remover Peça') 
    entrada = int(input('Digite o CÓDIGO desejado:')) 
    for pecas in listaPecas: 
        if (pecas['codigo'] == entrada): 
            listaPecas.remove(pecas) 
 
 
# Programa principal. 
 
meu_nome1234567 = 'Guilherme Oliveira Deodato de Souza' 
print('Bem vindo (a) ao controle de Estoque da Bicicletaria do {}'.format(meu_nome1234567)) 
 
while True: 
    try: 
        opcao = int(input('Escolha a opção desejada:\n' 
                          '1-Cadastrar Peças\n' 
                          '2-Consultar Peças\n' 
                          '3-Remover Peças\n' 
                          '4-Sair\n' 
                          '>>')) 
        if opcao == 1: 
            codigoPeca += 1 
            cadastrarPeca(codigoPeca) 
        elif opcao == 2: 
            consultarPeca() 
        elif opcao == 3: 
            removerPeca() 
        elif opcao == 4: 
            print('Encerrando programa...') 
            break 
        else: 
            print('Digite uma opção que esteja no menu.') 
    except ValueError: 
        print('Insira apenas valores numéricos inteiros.') 
 
# Fim do programa... 