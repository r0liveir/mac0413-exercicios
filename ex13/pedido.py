from abc import ABC, abstractmethod
import sys


class Pedido(ABC):
    @abstractmethod
    def preco(self) -> float:
        pass

    @abstractmethod
    def descricao(self) -> str:
        pass


class LancheBasico(Pedido):
    def preco(self) -> float:
        return 20.0

    def descricao(self) -> str:
        return "Lanche básico"


class PedidoDecorator(Pedido, ABC):
    def __init__(self, pedido: Pedido):
        # TODO
        raise NotImplementedError("Implemente o construtor do decorador")


class QueijoExtra(PedidoDecorator):
    def preco(self) -> float:
        # TODO
        raise NotImplementedError("Implemente preco")

    def descricao(self) -> str:
        # TODO
        raise NotImplementedError("Implemente descricao")


class EmbalagemEspecial(PedidoDecorator):
    def preco(self) -> float:
        # TODO
        raise NotImplementedError("Implemente preco")

    def descricao(self) -> str:
        # TODO
        raise NotImplementedError("Implemente descricao")


class TamanhoGrande(PedidoDecorator):
    def preco(self) -> float:
        # TODO
        raise NotImplementedError("Implemente preco")

    def descricao(self) -> str:
        # TODO
        raise NotImplementedError("Implemente descricao")


def main():
    decoradores = {
        "QUEIJO": QueijoExtra,
        "EMBALAGEM": EmbalagemEspecial,
        "GRANDE": TamanhoGrande,
    }
    pedido = LancheBasico()
    for codigo in sys.stdin.readline().split():
        pedido = decoradores[codigo](pedido)
    print(pedido.descricao())
    print(f"{pedido.preco():.2f}")


if __name__ == "__main__":
    main()
