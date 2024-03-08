import unittest
import mysql.connector

# Importe as funções do seu código
from seu_codigo import (
    conectar_banco,
    listar_musicas,
    inserir_musica,
    atualizar_musica,
    deletar_musica
)

class TestCRUDMusicas(unittest.TestCase):
    def setUp(self):
        # Configurações de conexão ao banco de dados de teste
        self.conn = mysql.connector.connect(
            host="localhost",
            port="3307",
            user="root",
            database="projetoLSD_teste"
        )
        self.cursor = self.conn.cursor()
        
        # Crie uma tabela de teste para músicas
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS musicas_teste (
                id INT AUTO_INCREMENT PRIMARY KEY,
                titulo VARCHAR(100) NOT NULL,
                duracao TIME,
                banda_id INT
            )
            """
        )
        self.conn.commit()

    def test_inserir_musica(self):
        inserir_musica("Título da Música", "00:03:30", 1)
        
        # Execute uma consulta para verificar se a música foi inserida corretamente
        self.cursor.execute("SELECT * FROM musicas_teste WHERE titulo = 'Título da Música'")
        musica = self.cursor.fetchone()
        
        self.assertIsNotNone(musica)
        self.assertEqual(musica[1], "Título da Música")
        self.assertEqual(musica[2], "00:03:30")
        self.assertEqual(musica[3], 1)

    def test_listar_musicas(self):
        # Insira algumas músicas de teste
        inserir_musica("Música 1", "00:04:00", 1)
        inserir_musica("Música 2", "00:03:45", 2)
        
        # Redirecionar a saída padrão para capturar a saída de print
        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            listar_musicas()
            output = out.getvalue().strip()
            self.assertIn("Música 1", output)
            self.assertIn("Música 2", output)
        finally:
            sys.stdout = saved_stdout

    def test_atualizar_musica(self):
        inserir_musica("Música Original", "00:04:00", 1)
        
        # Atualize a música
        atualizar_musica(1, "Música Atualizada", "00:05:00", 2)
        
        # Verifique se a música foi atualizada corretamente
        self.cursor.execute("SELECT * FROM musicas_teste WHERE id = 1")
        musica_atualizada = self.cursor.fetchone()
        
        self.assertIsNotNone(musica_atualizada)
        self.assertEqual(musica_atualizada[1], "Música Atualizada")
        self.assertEqual(musica_atualizada[2], "00:05:00")
        self.assertEqual(musica_atualizada[3], 2)

    def test_deletar_musica(self):
        inserir_musica("Música para Deletar", "00:03:30", 1)
        
        # Deletar a música
        deletar_musica(1)
        
        # Verifique se a música foi deletada corretamente
        self.cursor.execute("SELECT * FROM musicas_teste WHERE id = 1")
        musica_deletada = self.cursor.fetchone()
        
        self.assertIsNone(musica_deletada)

    def tearDown(self):
        # Limpeza após os testes
        self.cursor.execute("DROP TABLE IF EXISTS musicas_teste")
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    unittest.main()
