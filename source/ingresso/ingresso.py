from wsgiref.validate import validator


class Ingresso:
    def __init__(self, id, valor, descricao):
        self.id = id
        self.valor = valor
        self.descricao = descricao
        self.vendido = False
        self.comprador = None