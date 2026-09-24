// Atividade.java

import java.util.ArrayList;
import java.util.List;


class Tarefa {

    private final int id;
    private final String descricao;
    private boolean concluida;

    public Tarefa(int id, String descricao) {
        this.id = id;
        this.descricao = descricao;
        this.concluida = false;
    }

    public int getId() {
        return id;
    }

    public String getDescricao() {
        return descricao;
    }

    public boolean isConcluida() {
        return concluida;
    }

    public void concluir() {
        concluida = true;
    }
}


class QuadroTarefas {

    /*
     * Model da aplicação.
     * Responsável por armazenar e modificar as tarefas.
     */

    private final List<Tarefa> tarefas;
    private int proximoId;

    public QuadroTarefas() {
        tarefas = new ArrayList<>();
        proximoId = 1;
    }

    public Tarefa adicionar(String descricao) {
        // TODO
        return null;
    }

    public boolean concluir(int idTarefa) {
        // TODO
        return false;
    }

    public boolean remover(int idTarefa) {
        // TODO
        return false;
    }

    public List<Tarefa> listar() {
        // TODO
        return null;
    }
}


class ListaView {

    /*
     * View responsável pela apresentação detalhada das tarefas.
     */

    public String renderizar(List<Tarefa> tarefas) {
        // TODO
        return null;
    }
}


class ResumoView {

    /*
     * View responsável pela apresentação resumida das tarefas.
     */

    public String renderizar(List<Tarefa> tarefas) {
        // TODO
        return null;
    }
}


class TarefaController {

    /*
     * Controller da aplicação.
     * Interpreta comandos e coordena Model e Views.
     */

    private final QuadroTarefas model;
    private final ListaView listaView;
    private final ResumoView resumoView;

    public TarefaController(
            QuadroTarefas model,
            ListaView listaView,
            ResumoView resumoView) {

        this.model = model;
        this.listaView = listaView;
        this.resumoView = resumoView;
    }

    public String executar(String comando) {
        // TODO
        return null;
    }
}


public class Atividade {

    /*
     * Esta classe existe apenas para definir o arquivo principal da entrega.
     * Não é necessário implementar um método main.
     */
}