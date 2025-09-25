import unittest
from unittest.mock import patch
import tempfile
import shutil
from pathlib import Path
import sys
import io
from contextlib import redirect_stdout

# Adiciona o diretório do projeto ao path para encontrar o módulo cli
project_dir = Path(__file__).parent.parent
sys.path.insert(0, str(project_dir))

from specbook import cli

class Args:
    """Objeto simples para simular o namespace de argparse."""
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

class TestSpecBookCli(unittest.TestCase):
    """Testes para o SpecBook CLI."""

    def setUp(self):
        """Cria um diretório temporário para cada teste."""
        self.test_dir = Path(tempfile.mkdtemp())
        self.project_path = self.test_dir / "mybook"
        init_args = Args(project=str(self.project_path), func=cli.cmd_init)
        cli.cmd_init(init_args)

    def tearDown(self):
        """Remove o diretório temporário após cada teste."""
        shutil.rmtree(self.test_dir)

    def test_generate_scene(self):
        """Testa o comando 'generate scene'."""
        # 1. Criar specs de personagem e cenário
        char_data = {"name": "Luna", "desire": "Encontrar a relíquia", "fear": "O escuro"}
        cli.write_file(
            self.project_path / "specs" / "characters" / "luna.yaml",
            cli.to_yaml(char_data)
        )
        setting_data = {"world": {"name": "Aethelgard", "mood": "Sombrio e chuvoso"}}
        cli.write_file(
            self.project_path / "specs" / "settings" / "aethelgard.yaml",
            cli.to_yaml(setting_data)
        )

        # 2. Rodar o comando generate de forma não-interativa
        args = Args(
            project=str(self.project_path),
            generate_type="scene",
            character="Luna",
            setting="Aethelgard",
            func=cli.cmd_generate
        )
        cli.cmd_generate(args)

        # 3. Verificar se o arquivo foi criado
        scene_path = self.project_path / "fragments" / "scenes" / "scene_luna_em_aethelgard.md"
        self.assertTrue(scene_path.exists())

        # 4. Verificar o conteúdo do arquivo
        content = scene_path.read_text()
        self.assertIn("Cena: Luna em Aethelgard", content)
        self.assertIn("Personagem: Luna (Desejo: Encontrar a relíquia, Medo: O escuro)", content)
        self.assertIn("Cenário: Aethelgard (Atmosfera: Sombrio e chuvoso)", content)

# Adicione este teste ao seu arquivo test_specbook.py existente
# Lembre-se de que os outros testes foram omitidos aqui por brevidade

if __name__ == "__main__":
    unittest.main()
