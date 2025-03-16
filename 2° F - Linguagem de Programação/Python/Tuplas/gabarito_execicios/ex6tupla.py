# 6)	Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar para cada palavra, quais são as suas vogais.

tupla = ('abacaxi', 'banana', 'uva', 'jilo', 'ameixa')

for palavra in tupla:
    print(palavra)
    for letra in palavra:
        if letra in 'aeiou':
            print(letra)