# #4)	Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# a.	Quantas vezes apareceu o número 9;
# b.	Em que posição foi digitado o primeiro valor 3;
# c.	Quais foram os números pares.

tupla = ()
for i in range(4):
    valor = int(input('Digite um numero: '))
    tupla += (valor, )
print(tupla)

#a
valor = 9
if valor in tupla:
    print(f'o Valor 9 apareceu {tupla.count(valor)} vezes')
else:
    print('valor não está na tupla')

#b
valor = 3
if valor in tupla:
    print(f'o Valor 3 está na posição {tupla.index(valor)} ')
else:
    print('valor não está na tupla')

#c
for i in tupla:
    if i % 2 == 0:
        print({i})
