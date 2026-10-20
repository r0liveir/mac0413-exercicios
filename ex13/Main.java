import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Locale;

interface Pedido {
    double preco();
    String descricao();
}

class LancheBasico implements Pedido {
    @Override
    public double preco() {
        return 20.0;
    }

    @Override
    public String descricao() {
        return "Lanche básico";
    }
}

abstract class PedidoDecorator implements Pedido {
    protected final Pedido pedidoDecorado;

    public PedidoDecorator(Pedido pedido) {
        // TODO
        throw new UnsupportedOperationException("Implemente o construtor do decorador");
    }
}

class QueijoExtra extends PedidoDecorator {
    public QueijoExtra(Pedido pedido) {
        super(pedido);
    }

    @Override
    public double preco() {
        // TODO
        throw new UnsupportedOperationException("Implemente preco");
    }

    @Override
    public String descricao() {
        // TODO
        throw new UnsupportedOperationException("Implemente descricao");
    }
}

class EmbalagemEspecial extends PedidoDecorator {
    public EmbalagemEspecial(Pedido pedido) {
        super(pedido);
    }

    @Override
    public double preco() {
        // TODO
        throw new UnsupportedOperationException("Implemente preco");
    }

    @Override
    public String descricao() {
        // TODO
        throw new UnsupportedOperationException("Implemente descricao");
    }
}

class TamanhoGrande extends PedidoDecorator {
    public TamanhoGrande(Pedido pedido) {
        super(pedido);
    }

    @Override
    public double preco() {
        // TODO
        throw new UnsupportedOperationException("Implemente preco");
    }

    @Override
    public String descricao() {
        // TODO
        throw new UnsupportedOperationException("Implemente descricao");
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader leitor = new BufferedReader(new InputStreamReader(System.in));
        String linha = leitor.readLine();
        Pedido pedido = new LancheBasico();
        if (linha != null && !linha.trim().isEmpty()) {
            for (String codigo : linha.trim().split("\\s+")) {
                switch (codigo) {
                    case "QUEIJO": pedido = new QueijoExtra(pedido); break;
                    case "EMBALAGEM": pedido = new EmbalagemEspecial(pedido); break;
                    case "GRANDE": pedido = new TamanhoGrande(pedido); break;
                    default: throw new IllegalArgumentException("Código inválido: " + codigo);
                }
            }
        }
        System.out.println(pedido.descricao());
        System.out.printf(Locale.US, "%.2f%n", pedido.preco());
    }
}