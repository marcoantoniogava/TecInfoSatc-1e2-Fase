from functools import reduce
def media(x,y):
    return (x + y) / len(lista)

lista = [1,2,3,4,5,6,7]

resultado = reduce(media, lista)
print(resultado)