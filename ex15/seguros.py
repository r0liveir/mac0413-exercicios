class HistoricoCredito:
    def __init__(self, bloqueados):
        self.bloqueados = set(bloqueados)

    def consultar(self, cliente):
        return cliente not in self.bloqueados


class AvaliadorRisco:
    def __init__(self, limite):
        self.limite = limite

    def avaliar(self, valor):
        return valor <= self.limite


class EmissorApolice:
    def __init__(self, prefixo):
        self.prefixo = prefixo

    def emitir(self, proposta):
        return self.prefixo + proposta


class MediadorSeguros:
    def __init__(self, credito, risco, emissor):
        self.credito = credito
        self.risco = risco
        self.emissor = emissor

    def processar(self, proposta, cliente, valor):
        if not self.credito.consultar(cliente):
            return "RECUSADA:CREDITO"
        if not self.risco.avaliar(valor):
            return "RECUSADA:RISCO"
        return "APROVADA:" + self.emissor.emitir(proposta)


if __name__ == "__main__":
    mediador = MediadorSeguros(
        HistoricoCredito({"BLOQUEADO"}), AvaliadorRisco(1000), EmissorApolice("AP-")
    )
    print(mediador.processar("P1", "ANA", 500))
    print(mediador.processar("P2", "BLOQUEADO", 500))
    print(mediador.processar("P3", "ANA", 1500))
