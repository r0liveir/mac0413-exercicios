class EstoqueInsuficienteException(Exception):
    pass


class SaldoInsuficienteException(Exception):
    pass


class Estoque:

    def __init__(self, quantidade_inicial):
        # TODO
        pass

    def reservar(self, quantidade):
        # TODO
        pass

    def devolver(self, quantidade):
        # TODO
        pass

    def get_quantidade(self):
        # TODO
        pass


class Carteira:

    def __init__(self, saldo_inicial):
        # TODO
        pass

    def cobrar(self, valor):
        # TODO
        pass

    def get_saldo(self):
        # TODO
        pass


class ProcessadorPedido:

    @staticmethod
    def processar(estoque, carteira, quantidade, preco_unitario):
        # TODO
        pass