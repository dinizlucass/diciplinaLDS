import mysql.connector

def conectar_banco():
    # Conectar ao banco de dados MySQL
    conexao = mysql.connector.connect(
        host="127.0.0.1",
        port="3307",
        user="root",
        database="projetoLSD"
    )
    return conexao

def listar_bandas():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    consulta = "SELECT * FROM bandas"
    cursor.execute(consulta)
    resultados = cursor.fetchall()

    for linha in resultados:
        print(linha)

    cursor.close()
    conexao.close()

def inserir_banda(nome, genero, ano_formacao, integrantes, cidade_origem):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    consulta = "INSERT INTO bandas (nome, genero, ano_formacao, integrantes, cidade_origem) VALUES (%s, %s, %s, %s, %s)"
    valores = (nome, genero, ano_formacao, integrantes, cidade_origem)
    cursor.execute(consulta, valores)

    conexao.commit()
    print("Banda inserida com sucesso!")

    cursor.close()
    conexao.close()

def atualizar_banda(banda_id, nome, genero, ano_formacao, integrantes, cidade_origem):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    consulta = "UPDATE bandas SET nome=%s, genero=%s, ano_formacao=%s, integrantes=%s, cidade_origem=%s WHERE id=%s"
    valores = (nome, genero, ano_formacao, integrantes, cidade_origem, banda_id)
    cursor.execute(consulta, valores)

    conexao.commit()
    print("Banda atualizada com sucesso!")

    cursor.close()
    conexao.close()

def deletar_banda(banda_id):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    consulta = "DELETE FROM bandas WHERE id=%s"
    valores = (banda_id,)
    cursor.execute(consulta, valores)

    conexao.commit()
    print("Banda deletada com sucesso!")

    cursor.close()
    conexao.close()

# Exemplo de uso:

# Listar todas as bandas
# print("Listagem de todas as bandas:")
# listar_bandas()

#Inserir uma nova banda
# inserir_banda("Nome da Banda", "Gênero", 2000, 4, "Cidade")

# Atualizar uma banda existente
# atualizar_banda(1, "testebanda", "testegenero", 1990, 5, "cidadeteste")

# Deletar uma banda existente
# deletar_banda(21)
