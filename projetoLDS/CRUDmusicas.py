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

def listar_musicas():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    consulta = "SELECT * FROM musicas"
    cursor.execute(consulta)
    resultados = cursor.fetchall()

    for linha in resultados:
        print(linha)

    cursor.close()
    conexao.close()

def inserir_musica(titulo, duracao, banda_id):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    consulta = "INSERT INTO musicas (titulo, duracao, banda_id) VALUES (%s, %s, %s)"
    valores = (titulo, duracao, banda_id)
    cursor.execute(consulta, valores)

    conexao.commit()
    print("Música inserida com sucesso!")

    cursor.close()
    conexao.close()

def atualizar_musica(musica_id, titulo, duracao, banda_id):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    consulta = "UPDATE musicas SET titulo=%s, duracao=%s, banda_id=%s WHERE id=%s"
    valores = (titulo, duracao, banda_id, musica_id)
    cursor.execute(consulta, valores)

    conexao.commit()
    print("Música atualizada com sucesso!")

    cursor.close()
    conexao.close()

def deletar_musica(musica_id):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    consulta = "DELETE FROM musicas WHERE id=%s"
    valores = (musica_id,)
    cursor.execute(consulta, valores)

    conexao.commit()
    print("Música deletada com sucesso!")

    cursor.close()
    conexao.close()


# Listar todas as músicas
print("Listagem de todas as músicas:")
listar_musicas()

# Inserir uma nova música
# inserir_musica("Título da Música", "00:03:30", 1)

# Atualizar uma música existente
# atualizar_musica(1, "Novo Título da Música", "00:04:00", 1)

# Deletar uma música existente
# deletar_musica(1)
