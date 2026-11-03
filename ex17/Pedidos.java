import java.util.ArrayList;
import java.util.List;

public class Pedidos {
    public static void main(String[] args) {
    }
}

interface Observador {
    void atualizar(int numeroPedido, String novoEstado);
}

class Pedido {
    private final int numero;
    private String estado = "RECEBIDO";
    private final List<Observador> observadores = new ArrayList<>();

    public Pedido(int numero) {
        this.numero = numero;
    }

    public int getNumero() { return numero; }
    public String getEstado() { return estado; }

    public void inscrever(Observador observador) {
        throw new UnsupportedOperationException();
    }

    public void remover(Observador observador) {
        throw new UnsupportedOperationException();
    }

    public void mudarEstado(String novoEstado) {
        throw new UnsupportedOperationException();
    }
}

class PainelAcompanhamento implements Observador {
    private final List<String> historico = new ArrayList<>();

    public void atualizar(int numeroPedido, String novoEstado) {
        throw new UnsupportedOperationException();
    }

    public List<String> getHistorico() { return historico; }
}

class AvisoRetirada implements Observador {
    private final List<Integer> avisos = new ArrayList<>();

    public void atualizar(int numeroPedido, String novoEstado) {
        throw new UnsupportedOperationException();
    }

    public List<Integer> getAvisos() { return avisos; }
}