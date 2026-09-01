class EstoqueInsuficienteException(Exception):
    pass


class SaldoInsuficienteException(Exception):
    pass


class Estoque:
    def __init__(self, quantidade_inicial):
        if quantidade_inicial < 0:
            raise ValueError()
        self.quantidade = quantidade_inicial

    def reservar(self, quantidade):
        if quantidade <= 0:
            raise ValueError()
        elif quantidade > self.quantidade:
            raise EstoqueInsuficienteException()
        
        self.quantidade -= quantidade
        return True

    def devolver(self, quantidade):
        if quantidade <= 0: 
            raise ValueError()
        self.quantidade += quantidade

    def get_quantidade(self):
        return self.quantidade


class Carteira:
    def __init__(self, saldo_inicial):
        if saldo_inicial < 0:
            raise ValueError()
        self.saldo_disponivel = saldo_inicial

    def cobrar(self, valor):
        if valor <= 0:
            raise ValueError()
        elif valor > self.saldo_disponivel:
            raise SaldoInsuficienteException()

        self.saldo_disponivel -= valor

    def get_saldo(self):
        return self.saldo_disponivel


class ProcessadorPedido:
    @staticmethod
    def processar(estoque, carteira, quantidade, preco_unitario):
        if quantidade <= 0 or preco_unitario <= 0:
            raise ValueError()

        fez_reserva = False 

        try:
            fez_reserva = estoque.reservar(quantidade)
            carteira.cobrar(quantidade * preco_unitario)
        except EstoqueInsuficienteException:
            return "Estoque insuficiente"
        except SaldoInsuficienteException:
            if fez_reserva:
                estoque.devolver(quantidade)
            return "Saldo insuficiente"
        else:
            return "Pedido confirmado"
