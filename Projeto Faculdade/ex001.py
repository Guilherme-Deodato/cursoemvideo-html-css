#Inicio do programa e identificação 
identificador_4058452 = 'Guilherme Oliveira Deodato de Souza!' 
print('Bem vindo (a) a loja do {}'.format(identificador_4058452)) 
 
#Entradas para processamento. 
id_valor = float(input('Entre com o valor do produto: ')) 
id_quantidade = int(input('Entre com o valor da quantidade:')) 
 
#Ssitema de processamento. 
if id_quantidade <= 9: 
    desconto = 0 
    valor_total = id_valor * id_quantidade 
    valor_desconto = valor_total - (valor_total * desconto) 
    # Saída do sistema. 
    print('O valor sem desconto foi: R$ {:.2f}'.format(valor_total)) 
    print('O valor com desconto foi: R$ {:.2f} (desconto {:.0f}%)'.format(valor_desconto, desconto * 100)) 
 
elif id_quantidade < 100: 
    desconto = 5/100 
    valor_total = id_valor * id_quantidade 
    valor_desconto = valor_total - (valor_total * desconto) 
    # Saída do sistema. 
    print('O valor sem desconto foi: R$ {:.2f}'.format(valor_total)) 
    print('O valor com desconto foi: R$ {:.2f} (desconto {:.0f}%)'.format(valor_desconto, desconto * 100)) 
 
elif id_quantidade < 1000: 
    desconto = 10/100 
    valor_total = id_valor * id_quantidade 
    valor_desconto = valor_total - (valor_total * desconto) 
    # Saída do sistema. 
    print('O valor sem desconto foi: R$ {:.2f}'.format(valor_total)) 
    print('O valor com desconto foi: R$ {:.2f} (desconto {:.0f}%)'.format(valor_desconto, desconto * 100)) 
 
else: 
    desconto = 15/100 
    valor_total = id_valor * id_quantidade 
    valor_desconto = valor_total - (valor_total * desconto) 
    # Saída do sistema. 
    print('O valor sem desconto foi: R$ {:.2f}'.format(valor_total)) 
    print('O valor com desconto foi: R$ {:.2f} (desconto {:.0f}%)'.format(valor_desconto, desconto * 100)) 
#Fim do programa... 