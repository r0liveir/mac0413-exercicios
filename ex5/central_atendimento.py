from dataclasses import dataclass
from enum import Enum
from typing import List, Optional


class Prioridade(Enum):
    ALTA = 1
    MEDIA = 2
    BAIXA = 3


@dataclass(frozen=True)
class Chamado:
    id: str
    descricao: str
    prioridade: Prioridade


class CentralAtendimento:

    def __init__(self):
        
        self.chamados = {Prioridade.ALTA: [], Prioridade.MEDIA: [], Prioridade.BAIXA: []}
        self.presente = set()

    def adicionar(self, chamado: Chamado) -> bool:
        """
        Adiciona um chamado à central.

        Retorna:
            True  - se o chamado foi adicionado.
            False - se já existir um chamado pendente com o mesmo ID.
        """
        if (chamado.id in self.presente):
            return False
    
        self.presente.add(chamado.id)
        self.chamados[chamado.prioridade].append(chamado)
        return True

    def atender_proximo(self) -> Optional[Chamado]:
        """
        Remove e retorna o próximo chamado.

        Prioridade:
            ALTA > MEDIA > BAIXA

        Entre chamados da mesma prioridade deve ser respeitada
        a ordem de chegada.

        Retorna None caso não existam chamados pendentes.
        """

        for prioridade in (Prioridade.ALTA, Prioridade.MEDIA, Prioridade.BAIXA):
            if (self.chamados[prioridade]):
                return self.remove_prioridade(prioridade)
        return None

    def cancelar(self, id: str) -> bool:
        """
        Cancela um chamado pendente.

        Retorna:
            True  - se o chamado foi removido.
            False - se o ID não corresponder a um chamado pendente.
        """
        
        if (id not in self.presente):
            return False
        self.remove_id(id)
        return True

    def pendentes(self) -> List[Chamado]:
        """
        Retorna os chamados pendentes na ordem em que seriam atendidos.

        A consulta não deve alterar o estado da central.

        Modificar a lista retornada também não deve modificar
        a central.
        """
        
        return self.chamados[Prioridade.ALTA] + self.chamados[Prioridade.MEDIA] + self.chamados[Prioridade.BAIXA]

    def quantidade_pendentes(self) -> int:
        """
        Retorna a quantidade de chamados atualmente pendentes.
        """
        return len(self.presente)
    
    def remove_prioridade(self, prioridade: Prioridade) -> Chamado:
        chamado = self.chamados[prioridade].pop(0)
        self.presente.remove(chamado.id)
        return chamado
    
    def remove_id(self, id: str) -> None:
        
        self.presente.remove(id)
        
        for prioridade in (self.chamados.values()):
            for i in range(len(prioridade)):
                if (prioridade[i].id == id):
                    prioridade.pop(i)
                    return
        