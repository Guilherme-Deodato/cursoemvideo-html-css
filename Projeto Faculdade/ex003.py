#Identificador pessoal. 
meu_nome1234567 = 'Guilherme Oliveira Deodato de Souza' 
print('Bem vindo a Companhia de logística do {} S.A.'.format(meu_nome1234567)) 
 
#Função que define o volume do objeto e retorna seu valor. 
def dimensoesObjeto(): 
 
    global valor_objeto 
    valor_objeto = 0 
 
    while True: 
        try: 
            altura = int(input('Digite a altura do objeto (em cm): ')) 
            comprimento = int(input('Digite o comprimento do objeto (em cm): ')) 
            largura = int(input('Digite a largura do objeto (em cm): ')) 
            volume = altura * largura * comprimento 
 
            if volume <= 1000: 
                valor_objeto = 10 
                print('O volume do objeto é (em cm³): {:.1f}'.format(volume)) 
                return valor_objeto 
            elif 1001 <= volume <= 10000: 
                valor_objeto = 20 
                print('O volume do objeto é (em cm³): {:.1f}'.format(volume)) 
                return valor_objeto 
            elif 10001 <= volume <= 30000: 
                valor_objeto = 30 
                print('O volume do objeto é (em cm³): {:.1f}'.format(volume)) 
                return valor_objeto 
            elif 30001 <= volume <= 100000: 
                    valor_objeto = 50 
                    print('O volume do objeto é (em cm³): {:.1f}'.format(volume)) 
                    return valor_objeto 
            elif volume >= 100000: 
                print('O volume do objeto é (em cm³): {:.1f}'.format(volume)) 
                print('Não aceitamos objetos com dimensões tão grandes') 
                print('Entre com dimensões desejadas novamente') 
                continue 
 
        except ValueError: 
            print('Você digitou alguma dimensão do objeto com valor não numérico') 
            print('Por favor entre com dimensões desejadas novamente') 
            continue 
 
#Função que define o peso do objeto e retorna o seu valor. 
def pesoObjeto(): 
 
    global valor_peso 
 
    while True: 
        try: 
            pesoKG = float(input('Digite o peso do objeto (em kg): ')) 
            if pesoKG <= 0.1: 
                valor_peso = 1 
                return valor_peso 
            elif 0.11 <= pesoKG <= 1: 
                valor_peso = 1.5 
                return valor_peso 
            elif 1.10 <= pesoKG <= 10: 
                valor_peso = 2 
                return valor_peso 
            elif 10.1 <= pesoKG <= 30: 
                valor_peso = 3 
                return valor_peso 
            elif pesoKG > 30: 
                print('Não aceitamos objetos tão pesados') 
                continue 
 
        except ValueError: 
            print('Você digitou peso do objeto com valor não numérico') 
 
#Função que define a rota de transporte do objeto e retorna o seu valor. 
def rotaObjeto(): 
 
    global valor_rota 
    valor_rota = 0 
 
    while (valor_rota == 0): 
        print('Selecione a rota: ') 
        print('RS - De Rio de Janeiro até São Paulo') 
        print('SR - São Paulo até Rio de Janeiro') 
        print('BS - De Brasília até São Paulo') 
        print('SB - De São Paulo até Brasília') 
        print('BR - Brasília até Rio de Janeiro') 
        print('RB - Rio de Janeiro até Brasília') 
        escolha_rota = input('>>') 
 
        if (escolha_rota == 'RS' or escolha_rota == 'SR'): 
            valor_rota = 1 
        elif (escolha_rota == 'BS' or escolha_rota == 'SB'): 
            valor_rota = 1.2 
        elif (escolha_rota == 'BR' or escolha_rota == 'RB'): 
            valor_rota = 1.5 
        else: 
            print('Você digitou uma rota que não existe') 
            print('Por favor entre com a rota desejada novamente') 
            continue 
 
    return valor_rota 
 
#Programa principal. 
dimensoesObjeto = (dimensoesObjeto()) 
pesoObjeto = (pesoObjeto()) 
rotaObjeto = (rotaObjeto()) 
 
#Resolução final do programa e exibição de resultados. 
total = valor_objeto * valor_peso * valor_rota 
print('Total a pagar (R$): {} (dimensões: {} * peso: {} * rota: {})'.format(total, valor_objeto, valor_peso, valor_rota)) 
#Fim do programa... 