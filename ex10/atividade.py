from abc import ABC, abstractmethod


# ============================================================
# ABSTRAÇÕES DOS PRODUTOS
# NÃO MODIFICAR, POR FAVOR
# ============================================================

class Veiculo(ABC):
    @abstractmethod
    def nome(self):
        pass

    @abstractmethod
    def operar(self):
        pass


class Sensor(ABC):
    @abstractmethod
    def nome(self):
        pass

    @abstractmethod
    def coletar(self):
        pass


class Relatorio(ABC):
    @abstractmethod
    def gerar(self, resumo):
        pass


# ============================================================
# PRODUTOS CONCRETOS
# NÃO MODIFICAR, POR FAVOR
# ============================================================

class RoverDeserto(Veiculo):
    def nome(self):
        return "RoverDeserto"

    def operar(self):
        return "exploracao no deserto"


class RoverPolar(Veiculo):
    def nome(self):
        return "RoverPolar"

    def operar(self):
        return "exploracao polar"


class SensorTermico(Sensor):
    def nome(self):
        return "SensorTermico"

    def coletar(self):
        return "temperatura"


class SensorGelo(Sensor):
    def nome(self):
        return "SensorGelo"

    def coletar(self):
        return "espessura do gelo"


class RelatorioTexto(Relatorio):
    def gerar(self, resumo):
        return "TEXTO: " + resumo


class RelatorioDetalhado(Relatorio):
    def gerar(self, resumo):
        return "DETALHADO: " + resumo


# ============================================================
# ABSTRACT FACTORY
#
# Define o contrato para criação de uma família de
# equipamentos relacionados.
#
# NÃO MODIFICAR ESTA CLASSE, POR FAVOR.
# ============================================================

class EquipamentoFactory(ABC):

    @abstractmethod
    def criar_veiculo(self):
        pass

    @abstractmethod
    def criar_sensor(self):
        pass


# ============================================================
# SUA IMPLEMENTAÇÃO
#
# Complete as duas fábricas concretas.
# ============================================================

class DesertoFactory(EquipamentoFactory):

    def criar_veiculo(self):
        return RoverDeserto()

    def criar_sensor(self):
        return SensorTermico()


class PolarFactory(EquipamentoFactory):

    def criar_veiculo(self):
        return RoverPolar()

    def criar_sensor(self):
        return SensorGelo()


# ============================================================
# FACTORY METHOD
#
# O fluxo geral da missão já está implementado.
# As subclasses devem decidir qual relatório será criado
# por meio de criar_relatorio().
#
# NÃO MODIFICAR executar(), POR FAVOR.
# ============================================================

class Missao(ABC):

    @abstractmethod
    def criar_relatorio(self):
        pass

    def executar(self, veiculo, sensor):

        resumo = (
            veiculo.nome()
            + " | "
            + veiculo.operar()
            + " | "
            + sensor.nome()
            + " | "
            + sensor.coletar()
        )

        relatorio = self.criar_relatorio()

        return relatorio.gerar(resumo)


# ============================================================
# SUA IMPLEMENTAÇÃO
#
# Complete o Factory Method de cada tipo de missão.
# ============================================================

class MissaoRapida(Missao):

    def criar_relatorio(self):
        return RelatorioTexto()


class MissaoCientifica(Missao):

    def criar_relatorio(self):
        return RelatorioDetalhado()


# ============================================================
# INTEGRAÇÃO
#
# O planejador deve trabalhar apenas com as abstrações
# Missao e EquipamentoFactory.
# ============================================================

class PlanejadorMissoes:

    def executar_missao(self, missao, fabrica):
        
        return missao.executar(fabrica.criar_veiculo(), fabrica.criar_sensor())