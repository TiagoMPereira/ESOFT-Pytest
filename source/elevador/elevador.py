class Elevador:
    def __init__(self):
        self.movimento = 0 # 0 Parado, 1 Subindo, -1 descendo
        self.andar_atual = 0 # Térreo
        self.andar_maximo = 48
        self.andar_minimo = -2 # Subsolos

    def mover_um_andar(self, andar):
        if andar > self.andar_atual:
            self.movimento = 1
        elif andar < self.andar_atual:
            self.movimento = -1
        else:
            self.movimento = 0

        self.andar_atual += self.movimento

    def mover(self, andar):
        if andar > self.andar_maximo or andar < self.andar_minimo:
            raise ValueError("O andar desejado é inexistente")
            
        while self.andar_atual != andar:
            self.mover_um_andar(andar)
        self.movimento = 0

        return True

    def emergencia(self):

        if self.movimento != 0:
            self.movimento = 0

        