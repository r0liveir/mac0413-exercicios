"""Legado funcional: compare os métodos repetidos nos dois formatos."""
from abc import ABC, abstractmethod
from dataclasses import dataclass
import sys


@dataclass(frozen=True)
class Venda:
    nome: str
    quantidade: int
    preco_centavos: int


@dataclass(frozen=True)
class Resumo:
    quantidade: int
    total_centavos: int


class RepositorioVendas:
    def __init__(self, vendas):
        self._vendas = list(vendas)

    def consultar(self):
        return list(self._vendas)


class ArmazenamentoMemoria:
    def __init__(self):
        self._arquivos = {}

    def salvar(self, destino, conteudo):
        self._arquivos[destino] = conteudo

    def ler(self, destino):
        return self._arquivos[destino]


class RelatorioVendas(ABC):
    
    def gerar(self, vendas) -> str:
        resumo = self.resumir(vendas)
        return self.cabecalho() + self.corpo(vendas) + self.rodape(resumo)
    
    
    def resumir(self, vendas):
        quantidade = sum(venda.quantidade for venda in vendas)
        total = sum(venda.quantidade * venda.preco_centavos for venda in vendas)
        return Resumo(quantidade, total)
    
    @abstractmethod
    def cabecalho(self) -> str:
        pass
    
    @abstractmethod
    def corpo(self, vendas) -> str:
        pass
    
    @abstractmethod
    def rodape(self, resumo) -> str:
        pass
       

class RelatorioTexto(RelatorioVendas):

    def cabecalho(self):
        return "RELATORIO DE VENDAS\n"

    def corpo(self, vendas):
        return "".join(
            f"{v.nome} | qtd={v.quantidade} | unit={v.preco_centavos}"
            f" | subtotal={v.quantidade * v.preco_centavos}\n"
            for v in vendas
        )

    def rodape(self, resumo):
        return f"TOTAL | qtd={resumo.quantidade} | valor={resumo.total_centavos}\n"


class RelatorioCSV(RelatorioVendas):
    
    def cabecalho(self):
        return "produto;quantidade;unitario_centavos;subtotal_centavos\n"

    def corpo(self, vendas):
        return "".join(
            f"{v.nome};{v.quantidade};{v.preco_centavos};{v.quantidade * v.preco_centavos}\n"
            for v in vendas
        )

    def rodape(self, resumo):
        return f"TOTAL;{resumo.quantidade};;{resumo.total_centavos}\n"


class CentralRelatorios:
    
    def __init__(self, repositorio, armazenamento):
        self._repositorio = repositorio
        self._armazenamento = armazenamento
        
    def emitir(self, relatorio, destino):
        vendas = self._repositorio.consultar()
        conteudo = relatorio.gerar(vendas)
        self._armazenamento.salvar(destino, conteudo)
        return conteudo


def main():
    
    formatos = {
        "TEXTO": RelatorioTexto,
        "CSV": RelatorioCSV,
    }
    
    formato = sys.stdin.readline().strip()
    destino = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    
    vendas = []
    
    for _ in range(n):
        nome, quantidade, preco = sys.stdin.readline().rstrip("\n").split(";")
        vendas.append(Venda(nome, int(quantidade), int(preco)))

    repositorio = RepositorioVendas(vendas)
    armazenamento = ArmazenamentoMemoria()
    relatorio = formatos[formato]()
    # O cliente ainda precisa coordenar as operações do subsistema.
    conteudo = relatorio.gerar(repositorio.consultar())
    armazenamento.salvar(destino, conteudo)
    sys.stdout.write(armazenamento.ler(destino))


if __name__ == "__main__":
    main()