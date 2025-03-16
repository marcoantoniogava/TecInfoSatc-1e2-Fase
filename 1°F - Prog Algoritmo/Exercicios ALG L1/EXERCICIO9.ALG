Algoritmo "exercicio9"
var
lugares, sessao, ingresso: inteiro
totaldia, totalsemana, totalmes: real
inicio
escreva ("digite valor ingresso: ")
leia (ingresso)
escreva ("digite nr sessao: ")
leia (sessao)
escreva ("digite nr lugares: ")
leia (lugares)
totaldia := ingresso * sessao * lugares
escreva ("valor dia R$ : ", totaldia)
totalsemana := (ingresso * sessao * lugares) * 7
escreva ("valor semana R$ : ", totalsemana)
totalmes := (ingresso * sessao * lugares) * 30
escreva ("valor semana R$ : ", totalmes)
Fimalgoritmo