# Identificador. 
meu_nome1234567 = 'Guilherme Oliveira Deodato de Souza' 
print('bem vindo a lanchonete do {}'.format(meu_nome1234567)) 
 
# Cardápio. 
print(15 * '*', 'Cardápio', 15 * '*') 
print('|  Código  |         Descrição       | Valor |') 
print('|    100   |      Cachorro Quente    |  9,00 |') 
print('|    101   |   Cachorro Quente Duplo | 11,00 |') 
print('|    102   |            X-Egg        | 12,00 |') 
print('|    103   |          X-Salada       | 12,00 |') 
print('|    104   |           X-Bacon       | 14,00 |') 
print('|    105   |           X-Tudo        | 17,00 |') 
print('|    200   |     Refrigerante Lata   |  5,00 |') 
print('|    201   |        Chá Gelado       |  4,00 |') 
 
#Declaração de variáveis 
 
total = 0 
valor_100 = 9.00 
valor_101 = 11.00 
valor_102 = 12.00 
valor_103 = 12.00 
valor_104 = 14.00 
valor_105 = 17.00 
valor_200 = 5.00 
valor_201 = 4.00 
 
#Laço de repetição que realiza o pedido do usuário através da leitura do pedido por um input que recebe a entrada do pedido. 
while True: 
    codigo_produto = input('Entre com o código desejado:') 
    if (codigo_produto == '100'): 
        total = total + valor_100 
        print('Você pediu um Cachorro-Quente no valor de {:.2f}'.format(valor_100)) 
    elif (codigo_produto == '101'): 
        total = total + valor_101 
        print('Você pediu um Cachorro-Quente Duplo no valor de {:.2f}'.format(valor_101)) 
    elif (codigo_produto == '102'): 
        total = total + valor_102 
        print('Você pediu um X-Egg no valor de {:.2f}'.format(valor_102)) 
    elif (codigo_produto == '103'): 
        total = total + valor_103 
        print('Você pediu um X-Salada no valor de {:.2f}'.format(valor_103)) 
    elif (codigo_produto == '104'): 
        total = total + valor_104 
        print('Você pediu um X-Bacon no valor de {:.2f}'.format(valor_104)) 
    elif (codigo_produto == '105'): 
        total = total + valor_105 
        print('Você pediu um X-Tudo no valor de {:.2f}'.format(valor_105)) 
    elif (codigo_produto == '200'): 
        total = total + valor_200 
        print('Você pediu um Refrigerante Lata no valor de {:.2f}'.format(valor_200)) 
    elif (codigo_produto == '201'): 
        total = total + valor_201 
        print('Você pediu um Chá Gelado no valor de {:.2f}'.format(valor_201)) 
    else: 
        print('Opção Inválida') 
        continue 
 
    print('Deseja pedir mais alguma coisa ?') 
    print('1 - Sim') 
    print('0 - Não') 
    sair = input('>>') 
 
    if (sair == '1'): 
        continue 
    elif (sair == '0'): 
        break 
 
print('O total a ser pago é: {:.2f}'.format(total)) 
#Fim do programa... 