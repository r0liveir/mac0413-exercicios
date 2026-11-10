import re
import sys

from nucleo import Repositorio, RealizarEmprestimo


class SistemaEmprestimos(Repositorio):
    def __init__(self):
        self.equipamentos = {"MIC1", "CAM1", "TRI1"}
        self.emprestimos = {}

    def equipamento_existe(self, equipamento: str) -> bool:
        return equipamento in self.equipamentos

    def equipamento_ocupado(self, equipamento: str) -> bool:
        return equipamento in self.emprestimos

    def aluno_tem_emprestimo(self, aluno: str) -> bool:
        return any(emprestimo[0] == aluno for emprestimo in self.emprestimos.values())

    def registrar(self, aluno: str, equipamento: str) -> None:
        self.emprestimos[equipamento] = (aluno, equipamento)

def main():
    sistema = SistemaEmprestimos()
    servico = RealizarEmprestimo(sistema)
    for linha in sys.stdin:
        linha = linha.rstrip("\r\n").strip(" \t")
        if not linha:
            continue
        partes = re.split(r"[ \t]+", linha)
        if len(partes) != 3 or partes[0] != "EMPRESTAR":
            print("COMANDO_INVALIDO")
            continue
        print(servico.executar(partes[1], partes[2]))


if __name__ == "__main__":
    main()
