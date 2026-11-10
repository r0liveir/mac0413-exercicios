from typing import Protocol
from emprestimos import SistemaEmprestimos

class Repositorio(Protocol):
    
    def equipamento_existe(self, equipamento: str) -> bool: ...
    def equipamento_ocupado(self, equipamento: str) -> bool: ...
    def aluno_tem_emprestimo(self, aluno: str) -> bool: ...
    def registrar(self, aluno: str, equipamento: str) -> None: ...


class RealizarEmprestimo:
    def __init__(self, repositorio: Repositorio):
        self._repositorio = repositorio

    def executar(self, aluno: str, equipamento: str) -> str:
        if not self._repositorio.equipamento_existe(equipamento):
            return "INEXISTENTE"
        if self._repositorio.equipamento_ocupado(equipamento):
            return "INDISPONIVEL"
        if self._repositorio.aluno_tem_emprestimo(aluno):
            return "LIMITE_ALUNO"
        self._repositorio.registrar(aluno, equipamento)
        return "APROVADO"
