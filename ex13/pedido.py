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
        self._pedido_decorado = pedido


class QueijoExtra(PedidoDecorator):
    def preco(self) -> float:
        return self._pedido_decorado.preco() + 4

    def descricao(self) -> str:
        return self._pedido_decorado.descricao() + " + queijo extra"


class EmbalagemEspecial(PedidoDecorator):
    def preco(self) -> float:
        return self._pedido_decorado.preco() + 3

    def descricao(self) -> str:
        return self._pedido_decorado.descricao() + " + embalagem especial"


class TamanhoGrande(PedidoDecorator):
    def preco(self) -> float:
        return self._pedido_decorado.preco() * 1.5

    def descricao(self) -> str:
        return self._pedido_decorado.descricao() + " + tamanho grande"


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
