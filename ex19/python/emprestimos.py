import re
import sys


class SistemaEmprestimos:
    def __init__(self):
        self.equipamentos = {"MIC1", "CAM1", "TRI1"}
        self.emprestimos = {}

    def realizar(self, aluno, equipamento):
        if equipamento not in self.equipamentos:
            return "INEXISTENTE"
        if equipamento in self.emprestimos:
            return "INDISPONIVEL"
        if aluno in self.emprestimos.values():
            return "LIMITE_ALUNO"
        self.emprestimos[equipamento] = aluno
        return "APROVADO"


def main():
    sistema = SistemaEmprestimos()
    for linha in sys.stdin:
        linha = linha.rstrip("\r\n").strip(" \t")
        if not linha:
            continue
        partes = re.split(r"[ \t]+", linha)
        if len(partes) != 3 or partes[0] != "EMPRESTAR":
            print("COMANDO_INVALIDO")
            continue
        print(sistema.realizar(partes[1], partes[2]))


if __name__ == "__main__":
    main()
