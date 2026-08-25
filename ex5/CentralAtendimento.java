import java.util.List;
import java.util.Objects;

enum Prioridade {
    ALTA,
    MEDIA,
    BAIXA
}

final class Chamado {

    private final String id;
    private final String descricao;
    private final Prioridade prioridade;

    public Chamado(String id, String descricao, Prioridade prioridade) {
        this.id = Objects.requireNonNull(id);
        this.descricao = Objects.requireNonNull(descricao);
        this.prioridade = Objects.requireNonNull(prioridade);
    }

    public String getId() {
        return id;
    }

    public String getDescricao() {
        return descricao;
    }

    public Prioridade getPrioridade() {
        return prioridade;
    }

    @Override
    public String toString() {
        return id + " (" + prioridade + ")";
    }
}


public class CentralAtendimento {

    /*
     * Você pode criar aqui os atributos que considerar necessários.
     */

    public CentralAtendimento() {
        // TODO
    }

    /**
     * Adiciona um chamado à central.
     *
     * @return true se o chamado foi adicionado;
     *         false se já existir um chamado pendente com o mesmo ID.
     */
    public boolean adicionar(Chamado chamado) {
        // TODO
        throw new UnsupportedOperationException("Método não implementado");
    }

    /**
     * Remove e retorna o próximo chamado que deve ser atendido.
     *
     * Prioridade:
     * ALTA > MEDIA > BAIXA
     *
     * Para chamados da mesma prioridade, deve ser respeitada
     * a ordem de chegada.
     *
     * @return próximo chamado ou null se a central estiver vazia.
     */
    public Chamado atenderProximo() {
        // TODO
        throw new UnsupportedOperationException("Método não implementado");
    }

    /**
     * Cancela um chamado pendente.
     *
     * @return true se o chamado foi encontrado e removido;
     *         false caso contrário.
     */
    public boolean cancelar(String id) {
        // TODO
        throw new UnsupportedOperationException("Método não implementado");
    }

    /**
     * Retorna os chamados pendentes na ordem em que seriam atendidos.
     *
     * Este método NÃO deve alterar o estado da central.
     * Alterações na lista retornada também NÃO devem alterar
     * o estado interno da central.
     */
    public List<Chamado> pendentes() {
        // TODO
        throw new UnsupportedOperationException("Método não implementado");
    }

    /**
     * Retorna a quantidade de chamados atualmente pendentes.
     */
    public int quantidadePendentes() {
        // TODO
        throw new UnsupportedOperationException("Método não implementado");
    }
}