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
        nome = registro.nome.strip(" \t")
        detalhe = registro.detalhe.strip(" \t")
        return Item(nome, detalhe)

    def validar(self, item: Item) -> Optional[str]:
        
        if (item.nome == ""):
            return "NOME_VAZIO"
        
        if (
            not 1 <= len(item.detalhe) <= 9
            or not all("0" <= caractere <= "9" for caractere in item.detalhe)
            or int(item.detalhe) == 0
        ):
            return "QUANTIDADE_INVALIDA"
        
        return


class Equipamento:
    def converter(self, registro: Registro) -> Item:
        nome = registro.nome.strip(" \t")
        detalhe = registro.detalhe.strip(" \t")
        return Item(nome, detalhe)

    def validar(self, item: Item) -> Optional[str]:
        
        if (item.nome == ""):
            return "NOME_VAZIO"
    
        if (item.detalhe == ""):
            return "PATRIMONIO_VAZIO"
        
        return


class Importador:
    def executar(self, registros: Iterable[Registro], extensao: Extensao) -> Relatorio:
        
        relatorio = Relatorio()
        operacao = 1
        for registro in registros:

            item = extensao.converter(registro)
            motivo = extensao.validar(item)
            if motivo is None:
                relatorio.aceitos.append(item)
            else:
                relatorio.rejeitados.append(Rejeicao(operacao, motivo))
        
            operacao += 1
            
        return relatorio


if __name__ == "__main__":
    lote = [Registro(" Luvas ", " 12 "), Registro("Máscaras", "0"),
            Registro("Fita", "3")]
    resultado = Importador().executar(lote, Consumivel())
    for item in resultado.aceitos:
        print(f"ACEITO {item.nome} | {item.detalhe}")
    for rejeicao in resultado.rejeitados:
        print(f"REJEITADO {rejeicao.numero} | {rejeicao.motivo}")
