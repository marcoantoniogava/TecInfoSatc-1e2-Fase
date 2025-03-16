Algoritmo "exercicio11"
Var
valorfab: inteiro
valorfin: real
distribuidor: real
impostos: real
Inicio
escreva ("qual o valor de fabrica do carro: ")
leia (valorfab)
distribuidor := (valorfab * 0.2)
impostos := (valorfab * 0.35)
valorfin := (valorfab + distribuidor + impostos)
escreva ("valor final do carro R$ ", valorfin)
Fimalgoritmo