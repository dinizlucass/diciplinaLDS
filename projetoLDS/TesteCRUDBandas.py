import unittest
import mysql.connector

# Importe as funções do seu código
from seu_codigo import (
    conectar_banco,
    listar_bandas,
    inserir_banda,
    atualizar_banda,
    deletar_banda
)

class TestCRUDBandas(unittest.TestCase):
    def setUp(self):
        # Configurações de conexão ao banco de dados de teste
        self.conn = mysql.connector.connect(
            host="localhost",
            port="3307",
            user="root",
            database="projetoLSD_teste"
        )
        self.cursor = self.conn.cursor()
        
        # Crie uma tabela de teste para bandas
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS bandas_teste (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                genero VARCHAR(50),
                ano_formacao INT,
                integrantes INT,
                cidade_origem VARCHAR(100)
            )
            """
        )
        self.conn.commit()

    def test_inserir_banda(self):
        inserir_banda("Nome da Banda", "Gênero", 2000, 4, "Cidade")
        
        # Execute uma consulta para verificar se a banda foi inserida corretamente
        self.cursor.execute("SELECT * FROM bandas_teste WHERE nome = 'Nome da Banda'")
        banda = self.cursor.fetchone()
        
        self.assertIsNotNone(banda)
        self.assertEqual(banda[1], "Nome da Banda")

    def test_listar_bandas(self):
        # Insira algumas bandas de teste
        inserir_banda("Banda 1", "Rock", 1990, 5, "Cidade 1")
        inserir_banda("Banda 2", "Pop", 2000, 4, "Cidade 2")
        
        # Redirecionar a saída padrão para capturar a saída de print
        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            listar_bandas()
            output = out.getvalue().strip()
            self.assertIn("Banda 1", output)
            self.assertIn("Banda 2", output)
        finally:
            sys.stdout = saved_stdout

    def test_atualizar_banda(self):
        inserir_banda("Banda Original", "Rock", 2000, 4, "Cidade Original")
        
        # Atualize a banda
        atualizar_banda(1, "Banda Atualizada", "Pop", 2010, 5, "Nova Cidade")
        
        # Verifique se a banda foi atualizada corretamente
        self.cursor.execute("SELECT * FROM bandas_teste WHERE id = 1")
        banda_atualizada = self.cursor.fetchone()
        
        self.assertIsNotNone(banda_atualizada)
        self.assertEqual(banda_atualizada[1], "Banda Atualizada")
        self.assertEqual(banda_atualizada[3], 2010)
        self.assertEqual(banda_atualizada[4], 5)
        self.assertEqual(banda_atualizada[5], "Nova Cidade")

    def test_deletar_banda(self):
        inserir_banda("Banda para Deletar", "Rock", 2000, 4, "Cidade para Deletar")
        
        # Deletar a banda
        deletar_banda(1)
        
        # Verifique se a banda foi deletada corretamente
        self.cursor.execute("SELECT * FROM bandas_teste WHERE id = 1")
        banda_deletada = self.cursor.fetchone()
        
        self.assertIsNone(banda_deletada)

    def tearDown(self):
        # Limpeza após os testes
        self.cursor.execute("DROP TABLE IF EXISTS bandas_teste")
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    unittest.main()
