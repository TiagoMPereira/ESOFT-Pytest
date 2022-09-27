import pytest

from source.elevador.elevador import Elevador

class TestElevador:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.elevador = Elevador()

    def test_elevador_em_movimento(self):
        assert self.elevador.movimento == 0

    def test_elevador_andar_inicial(self):
        assert self.elevador.andar_atual == 0