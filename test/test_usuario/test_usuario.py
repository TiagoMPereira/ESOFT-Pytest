import pytest

from source.usuario.usuario import Usuario

class TestUsuario:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.usuario = Usuario(id = 123456)

    def test_cria_usuario_com_id(self):
        assert self.usuario.id == 123456