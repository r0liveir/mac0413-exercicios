from dataclasses import dataclass, field
from typing import Iterable, Optional, Protocol


@dataclass(frozen=True)
class Registro:
    nome: str
    detalhe: str


@dataclass(frozen=True)
class Item:
    nome: str
    detalhe: str


@dataclass(frozen=True)
class Rejeicao:
    numero: int
    motivo: str


@dataclass
class Relatorio:
    aceitos: list[Item] = field(default_factory=list)
    rejeitados: list[Rejeicao] = field(default_factory=list)


class Extensao(Protocol):
    def converter(self, registro: Registro) -> Item: ...
    def validar(self, item: Item) -> Optional[str]: ...


class Consumivel:
    def converter(self, registro: Registro) -> Item:
        raise NotImplementedError

    def validar(self, item: Item) -> Optional[str]:
        raise NotImplementedError


class Equipamento:
    def converter(self, registro: Registro) -> Item:
        raise NotImplementedError

    def validar(self, item: Item) -> Optional[str]:
        raise NotImplementedError


class Importador:
    def executar(self, registros: Iterable[Registro], extensao: Extensao) -> Relatorio:
        raise NotImplementedError


if __name__ == "__main__":
    lote = [Registro(" Luvas ", " 12 "), Registro("Máscaras", "0"),
            Registro("Fita", "3")]
    resultado = Importador().executar(lote, Consumivel())
    for item in resultado.aceitos:
        print(f"ACEITO {item.nome} | {item.detalhe}")
    for rejeicao in resultado.rejeitados:
        print(f"REJEITADO {rejeicao.numero} | {rejeicao.motivo}")
