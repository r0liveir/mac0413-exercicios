class EstoqueInsuficienteException(Exception):
    pass


class SaldoInsuficienteException(Exception):
    pass


class Estoque:

    def __init__(self, quantidade_inicial):
        
        if (quantidade_inicial < 0):
            raise ValueError
        self.quantidade_disponivel = quantidade_inicial

    def reservar(self, quantidade):
        if (quantidade <= 0):
            raise ValueError
        
        elif (quantidade > self.get_quantidade()):
            raise EstoqueInsuficienteException
        
        else:
            self.quantidade_disponivel -= quantidade
            
        return

    def devolver(self, quantidade):
        if (quantidade <= 0):
            raise ValueError
        self.quantidade_disponivel += quantidade
        return

    def get_quantidade(self):
        return self.quantidade_disponivel


class Carteira:

    def __init__(self, saldo_inicial):
        if (saldo_inicial < 0):
            raise ValueError
        self.saldo = saldo_inicial

    def cobrar(self, valor):
        if (valor <= 0):
            raise ValueError
        elif (valor > self.get_saldo()):
            raise SaldoInsuficienteException
        else:
            self.saldo -= valor

    def get_saldo(self):
        return self.saldo


class ProcessadorPedido:

    @staticmethod
    def processar(estoque, carteira, quantidade, preco_unitario):
        
        if (quantidade <= 0 or preco_unitario <= 0):
            raise ValueError
        
        try:
            estoque.reservar(quantidade)
            carteira.cobrar(quantidade * preco_unitario)
        
        except EstoqueInsuficienteException:
            return "Estoque insuficiente"
        
        except SaldoInsuficienteException:
            estoque.devolver(quantidade)
            return "Saldo insuficiente"
            
        except Exception as e:
            raise e
            
        else:
            return "Pedido confirmado"
        
        
        