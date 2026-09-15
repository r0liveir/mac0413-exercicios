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
        return self.termometro.codigo()

    def medir(self):
        return (self.termometro.ler_fahrenheit() - 32) * 5 / 9


class SensorDigitalAdapter(Medidor):

    def __init__(self, sensor):
        self.sensor = sensor

    def get_id(self):
        return self.sensor.serial()

    def medir(self):
        
        if (self.sensor.esta_operacional() == False):
            raise SensorIndisponivelException

        return self.sensor.obter_leitura("C")


class CentralMonitoramento:
    
    _instance = None
    
    def __init__(self):
        self.medidores = {}

    @classmethod
    def get_instance(cls):
        if (cls._instance is None):
            cls._instance = CentralMonitoramento()
        return cls._instance


    def registrar(self, medidor):
        if (medidor.get_id() in self.medidores):
            raise MedidorJaRegistradoException
        self.medidores[medidor.get_id()] = medidor
        

    def remover(self, identificador):
        if (identificador not in self.medidores):
            return False
        self.medidores.pop(identificador)
        return True

    def quantidade(self):
        return len(self.medidores)

    def medir(self, identificador):
        if (identificador not in self.medidores):
            raise MedidorNaoEncontradoException
        return self.medidores[identificador].medir()

    def temperatura_media(self):
        temp = 0.0
        count = 0
        
        for medidor in self.medidores.values():
            try:
                temp += medidor.medir()
                count +=1
            except SensorIndisponivelException:
                continue
        return temp / count if count > 0 else 0.0

    def sensores_em_alerta(self, limite):
    
        identificadores = []
        
        for medidor in self.medidores.values():
                    try:
                        if (medidor.medir() > limite):
                            identificadores.append(medidor.get_id())
                    except SensorIndisponivelException:
                        continue    
        return identificadores