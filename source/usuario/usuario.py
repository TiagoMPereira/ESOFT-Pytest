
from source.elevador.elevador import Elevador

class Usuario:
    def __init__(self, id, elevador:Elevador):
        self.id = id
        self.elevador = elevador

    def chamar_elevador(self, andar_atual):
        status = False
        status = self.elevador.mover(andar_atual)
        if status == True:
            return "Chegou"
        return "Falha no elevador"


          