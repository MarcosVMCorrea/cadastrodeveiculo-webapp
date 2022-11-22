import mysql.connector
from mysql.connector import errorcode
print( 'conectando')
try:
    conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Macaviga_2442'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)
cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `oficina`;")

cursor.execute("CREATE DATABASE `oficina`;")

cursor.execute("USE `oficina`;")

# criando tabelas
TABLES = {}
TABLES['veiculos'] = ('''
      CREATE TABLE `veiculos` (
      `chassi` varchar(17) NOT NULL,
      `modelo` varchar(50) NOT NULL,
      `ano` int(4) NOT NULL,
      `placa` varchar(7) NOT NULL,
      `nome` varchar(20) NOT NULL,
      `cpfcnpj` varchar(20) NOT NULL,
      `telefone` varchar(11) NOT NULL,
      `cep` varchar(10) NOT NULL,
      PRIMARY KEY (`chassi`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['cliente'] = ('''
      CREATE TABLE `cliente` (
      `nome` varchar(20) NOT NULL,
      `chassi` varchar(17) NOT NULL,
      `cpfcnpj` varchar(20) NOT NULL,
      `telefone` varchar(11) NOT NULL,
      `cep` varchar(10) NOT NULL,
      PRIMARY KEY (`nome`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['ordemservico'] = ('''
      CREATE TABLE `ordemservico` (
      `id` int(6) NOT NULL AUTO_INCREMENT,
      `dataemissão` varchar(10) NOT NULL,
      `datafechamento` varchar(10) NOT NULL,
      `kilometragem` int(7) NOT NULL,
      `chassi` varchar(17) NOT NULL,
      `descricao` varchar(500) NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['usuario'] = ('''
      CREATE TABLE `usuario` (
      `nome` varchar(50) NOT NULL,
      `nickname` varchar(15) NOT NULL,
      `senha` varchar(100) NOT NULL,
      `categoria` varchar(6) NOT NULL,
      PRIMARY KEY (`nome`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('OK')
conn.commit()

cursor.close()
conn.close()