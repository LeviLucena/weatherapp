"""Script para executar os testes com o PYTHONPATH correto"""
import sys
import os
from pathlib import Path

# Adiciona o diretório raiz ao PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent))

# Agora importa e executa os testes
import unittest
from tests.test_api import TestWeatherAPI

if __name__ == "__main__":
    # Cria uma suite de testes
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestWeatherAPI)

    # Executa os testes
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Retorna código de saída apropriado
    sys.exit(0 if result.wasSuccessful() else 1)
