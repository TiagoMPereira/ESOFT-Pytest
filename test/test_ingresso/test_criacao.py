import pytest

from source.ingresso.ingresso import Ingresso

class TestIngresso:

    @pytest.fixture(autouse=True)
    def setup(self):
        id = "abc123"
        valor = 50.0
        descricao = "Show do DJ"
        self.ingresso = Ingresso(id = id, valor = valor, descricao=descricao)

    def test_cria_ingresso(self):
        assert self.ingresso.id == "abc123"
    
    def test_cria_ingresso_comprador(self):
        assert self.ingresso.comprador is None
    
    def test_cria_ingresso_vendido(self):
        assert self.ingresso.vendido is False