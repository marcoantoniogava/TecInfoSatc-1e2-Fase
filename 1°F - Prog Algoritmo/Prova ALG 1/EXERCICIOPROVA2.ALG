Algoritmo "exercicioprova2"
//Nome: Marco Antônio
Var
produto: caracter
quantidade: inteiro
preco: real
precototal: real
condicao: inteiro
resultado: real
Inicio
escreva ("informe nome produto: ")
leia (produto)
escreva ("informe quantidade: ")
leia (quantidade)
escreva ("informe o preço: ")
leia (preco)
precototal := quantidade * preco
//Utilizei * para multiplicaçao
escreva ("escolha condicao: 1 - À vista em dinheiro 10% desconto - 2 - À vista no cartão de crédito, recebe 5% de desconto - 3 - Em duas vezes, preço normal sem juros - 4 - Em três vezes, preço normal mais juros de 5% acréscimo")
leia (condicao)
se (condicao = 1) entao
//Utilizei * para multiplicaçao
resultado := (precototal * 0.9)
escreva ("total ao pagar: ", resultado)
fimse
se (condicao = 2) entao
//Utilizei * para multiplicaçao
resultado := (precototal * 0.95)
escreva ("total ao pagar: ", resultado)
fimse
se (condicao = 3) entao
//Utilizei * para multiplicaçao
resultado := (precototal * 0.5)
escreva ("total ao pagar por mês (2): ", resultado)
fimse
se (condicao = 4) entao
//Utilizei * para multiplicaçao e / para divisao
resultado := ((precototal / 3) * 1.05 * 1.05)
escreva ("total a pagar: ", resultado)
fimse
Fimalgoritmo