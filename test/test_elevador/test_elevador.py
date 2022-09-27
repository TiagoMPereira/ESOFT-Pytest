import pytest

from source.elevador.elevador import Elevador

class TestElevador:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.elevador = Elevador()

    def test_elevador_em_movimento(self):
        assert self.elevador.em_movimento == False