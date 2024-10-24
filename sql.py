import psycopg2

# Update connection string information
host = "localhost"
dbname = "postgres"
user = input("Nome de usuário:")
password = input("Senha:")
sslmode = "prefer"

# Construct connection string
if password == 'postgres' and user == 'postgres':
    conn_string = f'host={host} user={user} dbname={dbname} password={password} sslmode={sslmode}'
    conn = psycopg2.connect(conn_string)
    print("Connection established")

    cursor = conn.cursor()
else:
    print("USUÁRIO OU SENHA INCORRETOS")
# Drop previous table of same name if one exists
cursor.execute("DROP TABLE IF EXISTS inventário;")
print("Finished Dropping Table(If Existed)")

# Create a table
cursor.execute("CREATE TABLE IF NOT EXISTS inventário(id serial PRIMARY KEY,Local VARCHAR(50),"
               " nome VARCHAR(50), quantidade INTEGER, preço FLOAT,conta VARCHAR(200), valor_conta FLOAT);")
print("Finished creating table (if not existed)")

# Insert some data into the table
x = int(input("DIGITE QUANTAS SEQUÊNCIAS DE DADOS SERÃO INSERIDOS NESSA BASE:"))
y = str(input("DESEJA INSERIR DADOS DE COMPRAS FEITAS OU DE CONTAS PAGAS:"))
for i in range(1, x + 1):
    if y in ('compra','compras'):
        if i > 1:
            print("Proximo local")
        local = input("Local da compra:")
        nome = input("Nome da fruta:")
        quantidade = int(input("quantidade de fruta:"))
        preço = float(input("preço de cada fruta:"))
        cursor.execute("INSERT INTO inventário (local,nome, quantidade,preço,conta, valor_conta) "
                       "VALUES (%s, %s, %s, %s,NULL,NULL);", (local, nome, quantidade, preço))
    elif y in ('conta','contas'):
        conta = str(input("qual a conta:"))
        valor = float(input("valor da conta:"))
        cursor.execute("INSERT INTO inventário (local,nome, quantidade,preço,conta,valor_conta)"
                       " VALUES (NULL, NULL, NULL, NULL,%s,%s);", (conta, valor))
print("Inserted %s rows of data" % x)
c = str(input("Deseja realizar consuta:"))
if c == 'Sim' or c == 'sim':
    Z = int(input("Quantas consutas deseja realizar:"))
    for j in range(1, Z + 1):
        consulta = input("Insira a consulta:")
        cursor.execute(consulta, ";")
        z = cursor.fetchall()
        print(z)
        print("Dados inseridos e consultados")
else:
    print("Dados inseridos")
# Clean up

conn.commit()
cursor.close()
conn.close()
