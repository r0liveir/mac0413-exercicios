# atividade.py


class Tarefa:
    def __init__(self, id_tarefa, descricao):
        self._id = id_tarefa
        self._descricao = descricao
        self._concluida = False

    def get_id(self):
        return self._id

    def get_descricao(self):
        return self._descricao

    def esta_concluida(self):
        return self._concluida

    def concluir(self):
        self._concluida = True


class QuadroTarefas:
    """
    Model da aplicação.
    Responsável por armazenar e modificar as tarefas.
    """

    def __init__(self):
        self._tarefas = []
        self._proximo_id = 1

    def adicionar(self, descricao):
        tarefa = Tarefa(self._proximo_id, descricao)
        self._proximo_id += 1
        self._tarefas.append(tarefa)
        return tarefa

    def concluir(self, id_tarefa):
        for tarefa in self._tarefas:
            if tarefa.get_id() == id_tarefa:
                tarefa.concluir()
                return True

        return False

    def remover(self, id_tarefa):
        for tarefa in self._tarefas:
            if tarefa.get_id() == id_tarefa:
                self._tarefas.remove(tarefa)
                return True

        return False

    def listar(self):
        return self._tarefas


class ListaView:
    """
    View responsável pela apresentação detalhada das tarefas.
    """

    def renderizar(self, tarefas):
        if not tarefas:
            return "Nenhuma tarefa."

        return "\n".join(
            f'{tarefa.get_id()} - {tarefa.get_descricao()} [{"PENDENTE" if not tarefa.esta_concluida() else "CONCLUIDA"}]'
            for tarefa in tarefas
        )

class ResumoView:
    """
    View responsável pela apresentação resumida das tarefas.
    """

    def renderizar(self, tarefas):
        total = len(tarefas)
        concluidas = sum(1 for tarefa in tarefas if tarefa.esta_concluida())
        pendentes = total - concluidas

        return f"Total: {total}\nPendentes: {pendentes}\nConcluidas: {concluidas}"

class TarefaController:
    """
    Controller da aplicação.
    Interpreta os comandos e coordena Model e Views.
    """

    def __init__(self, model: QuadroTarefas, lista_view: ListaView, resumo_view: ResumoView):
        self._model = model
        self._lista_view = lista_view
        self._resumo_view = resumo_view

    def executar(self, comando):
        input = comando.split(';')
        if input[0] == "ADICIONAR":
            if len(input) != 2:
                return "COMANDO_INVALIDO"
            self._model.adicionar(input[1])
            return "OK"
        elif input[0] == "CONCLUIR":
            if len(input) != 2 or not input[1].isdigit():
                return "COMANDO_INVALIDO"
            success = self._model.concluir(int(input[1]))
            return "OK" if success else "NAO_ENCONTRADA"
        elif input[0] == "REMOVER":
            if len(input) != 2 or not input[1].isdigit():
                return "COMANDO_INVALIDO"
            success = self._model.remover(int(input[1]))
            return "OK" if success else "NAO_ENCONTRADA"
        elif input[0] == "LISTAR":
            return self._lista_view.renderizar(self._model.listar())
        elif input[0] == "RESUMO":
            return self._resumo_view.renderizar(self._model.listar())
        else:
            return "COMANDO_INVALIDO"
