import pytest

from source.usuario.usuario import Usuario
from source.elevador.elevador import Elevador

class TestUsuario:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.usuario = Usuario(id = 123456, elevador=Elevador())

    def test_cria_usuario_com_id(self):
        assert self.usuario.id == 123456

    def test_chama_elevador(self, mocker):
        andar_atual = 12
        mocker.patch("source.elevador.elevador.Elevador.mover", return_value = True)
        resp = self.usuario.chamar_elevador(andar_atual)
        assert resp == "Chegou"
