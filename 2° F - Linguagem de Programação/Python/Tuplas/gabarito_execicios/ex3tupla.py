#3)	Crie um programa que vai gerar cinco números aleatórios e colocar em uma tuplas. Depois disso, mostre a listagem de números gerados e indique o menor e o maior valor que estão na tupla.

tupla = ()
import  random 
for i in range(5):
    num = (random.randint(1, 10))
    tupla += (num,)
print(tupla)

valor_maximo = max(tupla)
valor_minino= min(tupla)

print(valor_maximo)
print(valor_minino)