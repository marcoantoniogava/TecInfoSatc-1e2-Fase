#1)	Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

tupla = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove', 'Vinte')

while True:
    valor = int(input('Digite um valor: '))
    if valor == 100:
        print('saindo do programa')
        break
    elif  valor <0 or valor > 20:
        print('valores inválidos')
        continue
    else:
        print(tupla[valor])
        
        