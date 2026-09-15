from abc import ABC, abstractmethod


class SensorIndisponivelException(Exception):
    pass


class MedidorJaRegistradoException(Exception):
    pass


class MedidorNaoEncontradoException(Exception):
    pass


class Medidor(ABC):

    @abstractmethod
    def get_id(self):
        pass

    @abstractmethod
    def medir(self):
        pass


# ============================================================
# COMPONENTES EXTERNOS
# POR FAVOR, NÃO MODIFICAR
# ============================================================

class TermometroAntigo:

    def __init__(self, codigo, temperatura_fahrenheit):
        self.__codigo = codigo
        self.__temperatura_fahrenheit = temperatura_fahrenheit

    def codigo(self):
        return self.__codigo

    def ler_fahrenheit(self):
        return self.__temperatura_fahrenheit


class SensorDigital:

    def __init__(self, serial, temperatura_celsius, operacional=True):
        self.__serial = serial
        self.__temperatura_celsius = temperatura_celsius
        self.__operacional = operacional

    def serial(self):
        return self.__serial

    def esta_operacional(self):
        return self.__operacional

    def obter_leitura(self, unidade):
        if unidade != "C":
            raise ValueError("Unidade não suportada")

        return self.__temperatura_celsius


# ============================================================
# A PARTIR DAQUI É SUA IMPLEMENTAÇÃO...
# ============================================================

class TermometroAdapter(Medidor):

    def __init__(self, termometro):
        self.termometro = termometro

    def get_id(self):
        raise NotImplementedError

    def medir(self):
        raise NotImplementedError


class SensorDigitalAdapter(Medidor):

    def __init__(self, sensor):
        self.sensor = sensor

    def get_id(self):
        raise NotImplementedError

    def medir(self):
        raise NotImplementedError


class CentralMonitoramento:

    @classmethod
    def get_instance(cls):
        raise NotImplementedError

    def registrar(self, medidor):
        raise NotImplementedError

    def remover(self, identificador):
        raise NotImplementedError

    def quantidade(self):
        raise NotImplementedError

    def medir(self, identificador):
        raise NotImplementedError

    def temperatura_media(self):
        raise NotImplementedError

    def sensores_em_alerta(self, limite):
        raise NotImplementedError