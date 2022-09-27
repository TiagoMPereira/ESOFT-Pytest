class Elevador:
    def __init__(self):
        self.movimento = 0 # 0 Parado, 1 Subindo, -1 descendo
        self.andar_atual = 0 # Térreo
        self.andar_maximo = 48
        self.andar_minimo = -2 # Subsolos