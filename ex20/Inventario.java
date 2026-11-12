import java.util.ArrayList;
import java.util.List;

public class Inventario {
    public static final class Registro {
        public final String nome;
        public final String detalhe;

        public Registro(String nome, String detalhe) {
            this.nome = nome;
            this.detalhe = detalhe;
        }
    }

    public static final class Item {
        public final String nome;
        public final String detalhe;

        public Item(String nome, String detalhe) {
            this.nome = nome;
            this.detalhe = detalhe;
        }
    }

    public static final class Rejeicao {
        public final int numero;
        public final String motivo;

        public Rejeicao(int numero, String motivo) {
            this.numero = numero;
            this.motivo = motivo;
        }
    }

    public static final class Relatorio {
        public final List<Item> aceitos = new ArrayList<>();
        public final List<Rejeicao> rejeitados = new ArrayList<>();
    }

    public interface Extensao {
        Item converter(Registro registro);
        String validar(Item item);
    }

    public static class Consumivel implements Extensao {
        @Override
        public Item converter(Registro registro) {
            throw new UnsupportedOperationException();
        }

        @Override
        public String validar(Item item) {
            throw new UnsupportedOperationException();
        }
    }

    public static class Equipamento implements Extensao {
        @Override
        public Item converter(Registro registro) {
            throw new UnsupportedOperationException();
        }

        @Override
        public String validar(Item item) {
            throw new UnsupportedOperationException();
        }
    }

    private static String limpar(String texto) {
        return texto.replaceAll("^[ \\t]+|[ \\t]+$", "");
    }

    public static class Importador {
        public Relatorio executar(Iterable<Registro> registros, Extensao extensao) {
            throw new UnsupportedOperationException();
        }
    }

    public static void main(String[] args) {
        List<Registro> lote = List.of(new Registro(" Luvas ", " 12 "),
                new Registro("Máscaras", "0"), new Registro("Fita", "3"));
        Relatorio resultado = new Importador().executar(lote, new Consumivel());
        for (Item item : resultado.aceitos) {
            System.out.println("ACEITO " + item.nome + " | " + item.detalhe);
        }
        for (Rejeicao rejeicao : resultado.rejeitados) {
            System.out.println("REJEITADO " + rejeicao.numero + " | " + rejeicao.motivo);
        }
    }
}