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
        # TODO
        pass

    def concluir(self, id_tarefa):
        # TODO
        pass

    def remover(self, id_tarefa):
        # TODO
        pass

    def listar(self):
        # TODO
        pass


class ListaView:
    """
    View responsável pela apresentação detalhada das tarefas.
    """

    def renderizar(self, tarefas):
        # TODO
        pass


class ResumoView:
    """
    View responsável pela apresentação resumida das tarefas.
    """

    def renderizar(self, tarefas):
        # TODO
        pass


class TarefaController:
    """
    Controller da aplicação.
    Interpreta os comandos e coordena Model e Views.
    """

    def __init__(self, model, lista_view, resumo_view):
        self._model = model
        self._lista_view = lista_view
        self._resumo_view = resumo_view

    def executar(self, comando):
        # TODO
        pass