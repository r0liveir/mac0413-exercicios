from abc import ABC, abstractmethod


class EstadoRobo(ABC):

    @abstractmethod
    def atacar(self, robo):
        pass

    @abstractmethod
    def receber_dano(self, robo, pontos):
        pass

    @abstractmethod
    def reparar(self, robo, pontos):
        pass

    @abstractmethod
    def nome(self):
        pass


class EstadoNormal(EstadoRobo):

    def atacar(self, robo):
        return robo.get_ataque_base()

    def receber_dano(self, robo, pontos):
        robo._reduzir_vida(pontos)
        
        if robo.get_vida_atual() == 0:
            robo.mudar_estado(EstadoDesativado())
        elif robo.get_vida_atual() / robo.get_vida_maxima() <= 0.5:
            robo.mudar_estado(EstadoCritico())

    def reparar(self, robo, pontos):
        robo._aumentar_vida(pontos)

    def nome(self):
        return "NORMAL"


class EstadoCritico(EstadoRobo):

    def atacar(self, robo):
        return 2 * robo.get_ataque_base()

    def receber_dano(self, robo, pontos):
        robo._reduzir_vida(pontos)
        
        if robo.get_vida_atual() == 0:
            robo.mudar_estado(EstadoDesativado())

    def reparar(self, robo, pontos):
        robo._aumentar_vida(pontos)
        if robo.get_vida_atual() / robo.get_vida_maxima() > 0.5:
            robo.mudar_estado(EstadoNormal())

    def nome(self):
        return "CRITICO"


class EstadoDesativado(EstadoRobo):

    def atacar(self, robo):
        return 0

    def receber_dano(self, robo, pontos):
        return

    def reparar(self, robo, pontos):
        return

    def nome(self):
        return "DESATIVADO"


class Robo:

    def __init__(self, modelo, vida_maxima, ataque_base, modulos=None):
        self._modelo = modelo
        self._vida_maxima = vida_maxima
        self._vida_atual = vida_maxima
        self._ataque_base = ataque_base
        self._modulos = list(modulos) if modulos is not None else []
        self._estado = EstadoNormal()

    def atacar(self):
        return self._estado.atacar(robo=self)

    def receber_dano(self, pontos):
        self._estado.receber_dano(self, pontos)

    def reparar(self, pontos):
        self._estado.reparar(self, pontos) 

    def clonar(self):
        robo = Robo(self._modelo, self._vida_maxima, self._ataque_base, self._modulos)
        robo._vida_atual = self._vida_atual
        robo._estado = self._estado

        return robo        

    def mudar_estado(self, novo_estado):
        self._estado = novo_estado

    def _reduzir_vida(self, pontos):
        if pontos > 0:
            self._vida_atual = max(0, self._vida_atual - pontos)

    def _aumentar_vida(self, pontos):
        if pontos > 0:
            self._vida_atual = min(
                self._vida_maxima,
                self._vida_atual + pontos
            )

    def adicionar_modulo(self, modulo):
        self._modulos.append(modulo)

    def get_modelo(self):
        return self._modelo

    def get_vida_maxima(self):
        return self._vida_maxima

    def get_vida_atual(self):
        return self._vida_atual

    def get_ataque_base(self):
        return self._ataque_base

    def get_modulos(self):
        return self._modulos

    def get_estado(self):
        return self._estado.nome()


class CatalogoRobos:

    def __init__(self):
        self._prototipos = {}

    def registrar(self, nome, prototipo):
        self._prototipos[nome] = prototipo

    def criar(self, nome):
        for key, val in self._prototipos.items():
            if key == nome:
                return val.clonar()
        else:
            raise ValueError()
