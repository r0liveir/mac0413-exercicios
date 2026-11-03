from abc import ABC, abstractmethod


class Observador(ABC):
    @abstractmethod
    def atualizar(self, numero_pedido, novo_estado):
        pass


class Pedido:
    def __init__(self, numero):
        self._numero = numero
        self._estado = "RECEBIDO"
        self._observadores = []

    def get_numero(self):
        return self._numero

    def get_estado(self):
        return self._estado

    def inscrever(self, observador):
        for inscrito in self._observadores:
            if inscrito is observador:
                return
        self._observadores.append(observador)

    def remover(self, observador):
        for indice, inscrito in enumerate(self._observadores):
            if inscrito is observador:
                del self._observadores[indice]
                return

    def mudar_estado(self, novo_estado):
        if (novo_estado != self._estado):
            self._estado = novo_estado
            for observador in self._observadores:
                observador.atualizar(self._numero, self._estado)

class PainelAcompanhamento(Observador):
    def __init__(self):
        self._historico = []

    def atualizar(self, numero_pedido, novo_estado):
        self._historico.append(f"{numero_pedido}:{novo_estado}")

    def get_historico(self):
        return self._historico


class AvisoRetirada(Observador):
    def __init__(self):
        self._avisos = []

    def atualizar(self, numero_pedido, novo_estado):
        if (novo_estado == "PRONTO"):
            self._avisos.append(numero_pedido)

    def get_avisos(self):
        return self._avisos
