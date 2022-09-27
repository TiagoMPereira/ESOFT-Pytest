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

    def test_elevador_mover_um_andar(self):
        andar_desejado = 1

        self.elevador.mover_um_andar(andar=andar_desejado)

        assert self.elevador.movimento != 0

    def test_elevador_mover_andar_final_subir(self):
        andar_desejado = 10

        self.elevador.mover(andar=andar_desejado)

        assert self.elevador.andar_atual == andar_desejado
    
    def test_elevador_mover_andar_final_descer(self):
        andar_desejado = -1

        self.elevador.mover(andar=andar_desejado)

        assert self.elevador.andar_atual == andar_desejado
    
    def test_elevador_mover_andar_final_parado(self):
        andar_desejado = -1

        self.elevador.mover(andar=andar_desejado)

        assert self.elevador.movimento == 0