import mysql.connector

conexao_banco = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '',
    database = 'vendas'
)

cursor = conexao_banco.cursor()

# CREATE

# nome = input('Digite o nome do produto: ')
# valor = float(input('Digite o valor do produto: '))

# comando_sql = f'INSERT INTO produtos (nome_produto, valor_produto) VALUES ("{nome}", {valor})'

# cursor.execute(comando_sql)
# conexao_banco.commit()

# UPDATE

# nome = input('Digite o nome do produto: ')
# id = int(input('Digite o id do produto: '))

# comando_sql = 'UPDATE produtos SET nome_produto = "{nome}" WHERE idprodutos  = {id}'
# cursor.execute(comando_sql)
# conexao_banco.commit()

# DELETE

# id = int(input('Digite o ID do produto que deseja excluir: '))

# comando_sql = f'DELETE FROM produtos WHERE idprodutos = {id}'
# cursor.execute(comando_sql)
# conexao_banco.commit()

# READ

comando_sql = 'SELECT * FROM produtos'
cursor.execute(comando_sql)
dados_tabela = cursor.fetchall()
print(dados_tabela)

print(dados_tabela[0][0]) #1
print(dados_tabela[1][1]) #sapato
print(dados_tabela[2][2]) #50

for i in dados_tabela:
    print(f'ID: {i[0]} PRODUTO: {i[1]} VALOR: {i[2]}')
    print(i) #Exibe tudo

id = int(input('Digite o id do produto: '))
for dados in dados_tabela:
    if dados[0] == id:
        nome_ou_valor = int(input('Digite 1 para mudar produto, 2 para mudar valor: '))
        if  nome_ou_valor == 1:
            nome = input('Digite o novo nome do produto: ')
            comando_sql = f'UPDATE produtos SET nome_produto = "{nome}" WHERE idprodutos  = {id}'
            cursor.execute(comando_sql)
            conexao_banco.commit()
        elif nome_ou_valor == 2:
            valor = float(input('Digite o novo valor do produto: '))
            comando_sql = f'UPDATE produtos SET valor_produto = "{valor}" WHERE idprodutos  = {id}'
            cursor.execute(comando_sql)
            conexao_banco.commit()
    else:
        print('ID não encontrado')


