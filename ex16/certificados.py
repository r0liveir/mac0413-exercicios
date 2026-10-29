from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class RegistroHistorico:
    acao: str
    estado_anterior: str
    estado_posterior: str


class OperacaoInvalida(RuntimeError):
    pass


class EstadoCertificado:
    def nome(self):
        raise NotImplementedError

    def alterar(self, certificado, placa):
        raise OperacaoInvalida("Alteracao nao permitida")

    def assinar(self, certificado):
        raise OperacaoInvalida("Assinatura nao permitida")

    def utilizar(self, certificado):
        raise OperacaoInvalida("Utilizacao nao permitida")

    def cancelar(self, certificado):
        raise OperacaoInvalida("Cancelamento nao permitido")

    def suspender(self, certificado):
        raise OperacaoInvalida("Suspensao nao permitida")

    def reativar(self, certificado):
        raise OperacaoInvalida("Reativacao nao permitida")


class NaoEmitido(EstadoCertificado):
    def nome(self):
        return "NAO_EMITIDO"


class Emitido(EstadoCertificado):
    def nome(self):
        return "EMITIDO"


class Suspenso(EstadoCertificado):
    def nome(self):
        return "SUSPENSO"


class Utilizado(EstadoCertificado):
    def nome(self):
        return "UTILIZADO"


class Cancelado(EstadoCertificado):
    def nome(self):
        return "CANCELADO"


class FabricaEstados:
    @staticmethod
    def criar(codigo):
        if codigo == "N":
            return NaoEmitido()
        raise ValueError("Codigo de estado desconhecido")


class Certificado:
    def __init__(self, numero, placa):
        self.numero = numero
        self.placa = placa
        self.estado = NaoEmitido()
        self._historico = []

    def nome_estado(self):
        return self.estado.nome()

    def trocar_estado(self, estado):
        self.estado = estado

    def historico(self):
        return tuple(self._historico)


    def alterar(self, placa):
        self.estado.alterar(self, placa)

    def assinar(self):
        self.estado.assinar(self)

    def utilizar(self):
        self.estado.utilizar(self)

    def cancelar(self):
        self.estado.cancelar(self)

    def suspender(self):
        self.estado.suspender(self)

    def reativar(self):
        self.estado.reativar(self)


class ParserRegistro(ABC):
    CAMPOS_PADRAO = (("numero", 4), ("placa", 7), ("estado", 1))

    def __init__(self, campos=None):
        self.campos = tuple(self.CAMPOS_PADRAO if campos is None else campos)

    def parse(self, linha):
        raise NotImplementedError

    @abstractmethod
    def criar_resultado(self):
        raise NotImplementedError

    @abstractmethod
    def atribuir(self, resultado, campo, valor):
        raise NotImplementedError


class ParserMapa(ParserRegistro):
    def criar_resultado(self):
        return {}

    def atribuir(self, resultado, campo, valor):
        raise NotImplementedError


class ParserCertificado(ParserRegistro):
    def criar_resultado(self):
        return Certificado("", "")

    def atribuir(self, resultado, campo, valor):
        raise NotImplementedError


if __name__ == "__main__":
    try:
        certificado = ParserCertificado().parse("0042ABC1234E")
        certificado.suspender()
        try:
            certificado.utilizar()
        except OperacaoInvalida:
            print("Utilizacao recusada enquanto suspenso")
        certificado.reativar()
        certificado.utilizar()
        print(certificado.numero, certificado.placa, certificado.nome_estado())
        for registro in certificado.historico():
            print(registro.acao, registro.estado_anterior, registro.estado_posterior)
    except (RuntimeError, ValueError) as erro:
        print(type(erro).__name__ + ": " + str(erro))
