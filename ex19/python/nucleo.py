from typing import Protocol


class Repositorio(Protocol):
    def equipamento_existe(self, equipamento: str) -> bool: ...
    def equipamento_ocupado(self, equipamento: str) -> bool: ...
    def aluno_tem_emprestimo(self, aluno: str) -> bool: ...
    def registrar(self, aluno: str, equipamento: str) -> None: ...


class RealizarEmprestimo:
    def __init__(self, repositorio: Repositorio):
        self._repositorio = repositorio

    def executar(self, aluno: str, equipamento: str) -> str:
        raise NotImplementedError
