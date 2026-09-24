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
        
    def __str__(self):
        
        return f"{self._id} - {self._descricao} [{'CONCLUIDA' if self._concluida else 'PENDENTE'}]"


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
        self._tarefas.append(tarefa)
        self._proximo_id += 1
        return tarefa

    def concluir(self, id_tarefa):
        
        for tarefa in self._tarefas:
            if (tarefa.get_id() == id_tarefa):
                tarefa.concluir()
                return True
            
        return False

    def remover(self, id_tarefa):
        for tarefa in self._tarefas:
            if (tarefa.get_id() == id_tarefa):
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
        
        if (tarefas == []):
            return "Nenhuma tarefa."
        
        strings = ""
        
        for tarefa in tarefas:
            strings += str(tarefa)
            strings += "\n"

        return strings[0:-1]

class ResumoView:
    """
    View responsável pela apresentação resumida das tarefas.
    """

    def renderizar(self, tarefas):
        
        total = len(tarefas)
        pendentes = 0
        concluidas = 0
        
        for tarefa in tarefas:
            
            if (tarefa.esta_concluida()):
                concluidas += 1
            else:
                pendentes += 1
                
        return f"Total: {total}\nPendentes: {pendentes}\nConcluidas: {concluidas}"


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
        
        comando = comando.split(";")
        
        if (comando[0] == "ADICIONAR"):
            if (len(comando) == 2):
                self._model.adicionar(comando[1])
                return "OK"

        elif (comando[0] == "CONCLUIR"):
            if ((len(comando) == 2) and (comando[1].isdigit())):
                if (self._model.concluir(int(comando[1]))):
                    return "OK"
                return "NAO_ENCONTRADA"
            
        elif (comando[0] == "REMOVER"):
            if ((len(comando) == 2) and (comando[1].isdigit())):
                if (self._model.remover(int(comando[1]))):
                    return "OK"
                return "NAO_ENCONTRADA"
            
        elif (comando[0] == "LISTAR"):
            return self._lista_view.renderizar(self._model.listar())
        
        elif (comando[0] == "RESUMO"):
            return self._resumo_view.renderizar(self._model.listar())
        

        return "COMANDO_INVALIDO"