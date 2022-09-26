import pytest

from source.ingresso.ingresso import Ingresso

def test_cria_ingresso():
    id = "abc123"
    ingresso = Ingresso(id = id)
    assert ingresso.id == id