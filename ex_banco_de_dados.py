import sqlite3

conexao = sqlite3.connect('banco_dados')
cursor = conexao.cursor()

#1. Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).
#cursor.execute('CREATE TABLE alunos(id INT,nome VARCHAR(100),idade INT,curso VARCHAR(100));')

#2. Insira pelo menos 5 registros de alunos na tabela 
#alunos_db = [
    #(1, 'Alan', 32, 'Engenharia'),
    #(2, 'Frederico', 25, 'Ciência da Computação'),
    #(3, 'Carol', 41, 'Medicina'),
    #(4, 'David', 19, 'Arquitetura'),
    #(5, 'Eva', 23, 'Engenharia')
#]
#cursor.executemany('INSERT INTO alunos VALUES (?, ?, ?, ?)', alunos_db)

#3. Consultas Básicas. Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecionar todos os registros da tabela "alunos".
#dados = cursor.execute('SELECT * FROM alunos')
#for alunos in dados:
 #   print(alunos)

#b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
#dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')
#for alunos in dados:
 #   print(alunos)

#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
#dados = cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome')
#for alunos in dados:
 #   print(alunos)

#d) Contar o número total de alunos na tabela
#dados = cursor.execute('SELECT COUNT(*) FROM alunos')
#for alunos in dados:
 #   print(alunos)

#4. Atualização e Remoção
#a) Atualize a idade de um aluno específico na tabela.
#cursor.execute('UPDATE alunos SET idade = 31 WHERE id = 1')


#b) Remova um aluno pelo seu ID.
#cursor.execute('DELETE FROM alunos WHERE id = 2')

#5. Criar uma Tabela e Inserir Dados
#Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) 
#e saldo (float). Insira alguns registros de clientes na tabela.

#cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY,nome VARCHAR(100),idade INT,saldo FLOAT);')
 
#clientes_db = [
    #(1, 'Debora', 32, 1350.25),
    #(2, 'Hugo', 35, 3725.52),
    #(3, 'Carol', 48, 5200),
    #(4, 'Gabriela', 19, 924.87),
    #(5, 'João', 53, 8723.42)
#]
#cursor.executemany('INSERT INTO clientes VALUES (?, ?, ?, ?)', clientes_db)

#6. Consultas e Funções Agregadas. Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
#dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')
#for clientes in dados:
 #   print(clientes)

#b) Calcule o saldo médio dos clientes.
#dados = cursor.execute('SELECT AVG(saldo) FROM clientes')
#for clientes in dados:
 #   print(clientes)

#c) Encontre o cliente com o saldo máximo.
#dados = cursor.execute('SELECT * FROM clientes WHERE saldo = (SELECT MAX(saldo) FROM clientes)')
#for clientes in dados:
 #   print(clientes)

#d) Conte quantos clientes têm saldo acima de 1000.
#dados = cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000')
#for clientes in dados:
    #print(clientes[0])

#7. Atualização e Remoção com Condições
#a) Atualize o saldo de um cliente específico.
#cursor.execute('UPDATE clientes SET saldo = 1850 WHERE id = 1')

#b) Remova um cliente pelo seu ID.
#cursor.execute('DELETE FROM clientes WHERE id = 3')

#8. Junção de Tabelas. Crie uma segunda tabela chamada "compras" com os campos: id(chave primária), 
#cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real). 
#Insira algumas compras associadas a clientes existentes na tabela "clientes".

#cursor.execute('CREATE TABLE compras(id INT PRIMARY KEY, cliente_id INT REFERENCES clientes(id),produto VARCHAR(100),valor REAL);')

#compras_db = [
    #(1, 1, 'Arroz', 35.99),
    #(2, 2, 'Banana', 13.50),
    #(3, 4, 'Arroz', 35.99),
    #(4, 5, 'Feijão', 6.99)

#]
#cursor.executemany('INSERT INTO compras VALUES (?, ?, ?, ?)', compras_db)

#Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.
dados = cursor.execute('''
                       SELECT 
                       clientes.nome AS nome_cliente,
                       compras.produto,
                       compras.valor 
                       FROM compras 
                       INNER JOIN clientes ON compras.cliente_id = clientes.id
                       ''')
for resultado in dados:
    print(f'Nome do Cliente: {resultado[0]}, Produto: {resultado[1]}, Valor: {resultado[2]}')


conexao.commit()
conexao.close