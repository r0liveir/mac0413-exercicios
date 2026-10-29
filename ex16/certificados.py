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
    
    def alterar(self, certificado, placa):
        certificado.placa = placa
        certificado._historico.append(RegistroHistorico("alterar", certificado.estado.nome(), certificado.estado.nome()))
        
    def assinar(self, certificado):
        certificado.trocar_estado(Emitido())
        certificado._historico.append(RegistroHistorico("assinar", NaoEmitido().nome(), Emitido().nome()))
        
    def cancelar(self, certificado):
        certificado.trocar_estado(Cancelado())
        certificado._historico.append(RegistroHistorico("cancelar", NaoEmitido().nome(), Cancelado().nome()))


class Emitido(EstadoCertificado):
    def nome(self):
        return "EMITIDO"
    
    def utilizar(self, certificado):
        certificado.trocar_estado(Utilizado())
        certificado._historico.append(RegistroHistorico("utilizar", Emitido().nome(), Utilizado().nome()))
        
    def cancelar(self, certificado):
        certificado.trocar_estado(Cancelado())
        certificado._historico.append(RegistroHistorico("cancelar", Emitido().nome(), Cancelado().nome()))
        
    def suspender(self, certificado):
        certificado.trocar_estado(Suspenso())
        certificado._historico.append(RegistroHistorico("suspender", Emitido().nome(), Suspenso().nome()))


class Suspenso(EstadoCertificado):
    def nome(self):
        return "SUSPENSO"
    
    def cancelar(self, certificado):
        certificado.trocar_estado(Cancelado())
        certificado._historico.append(RegistroHistorico("cancelar", Suspenso().nome(), Cancelado().nome()))
    
    def reativar(self, certificado):
        certificado.trocar_estado(Emitido())
        certificado._historico.append(RegistroHistorico("reativar", Suspenso().nome(), Emitido().nome()))


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
        elif codigo == "E":
            return Emitido()
        elif codigo == "S":
            return Suspenso()
        elif codigo == "U":
            return Utilizado()
        elif codigo == "C":
            return Cancelado()
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
        
        if (len(linha) != sum(tamanho for _, tamanho in self.campos)):
            raise ValueError()
        
        resultado = self.criar_resultado()
        inicio = 0

        for nome, tamanho in self.campos:
            fim = inicio + tamanho
            valor = linha[inicio:fim].strip()
            self.atribuir(resultado, nome, valor)
            inicio = fim

        return resultado

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
        resultado.update({campo: valor})


class ParserCertificado(ParserRegistro):
    def criar_resultado(self):
        return Certificado("", "")

    def atribuir(self, resultado, campo, valor):
        if campo == "numero":
            resultado.numero = valor
        elif campo == "placa":
            resultado.placa = valor
        elif campo == "estado":
            resultado.trocar_estado(FabricaEstados.criar(valor))
        else:
            raise ValueError()


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
