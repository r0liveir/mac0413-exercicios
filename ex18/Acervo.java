import java.util.List;

public class Acervo {
    public static void main(String[] args) {
    }
}

final class Edicao {
    private final String isbn;
    private final String titulo;
    private final String autor;
    private final List<Integer> capa;

    Edicao(String isbn, String titulo, String autor, List<Integer> capa) {
        throw new UnsupportedOperationException();
    }

    public String getIsbn() { return isbn; }
    public String getTitulo() { return titulo; }
    public String getAutor() { return autor; }
    public List<Integer> getCapa() { return capa; }
}

class FabricaEdicoes {
    public Edicao obter(String isbn, String titulo, String autor, List<Integer> capa) {
        throw new UnsupportedOperationException();
    }

    public int quantidadeEdicoes() {
        throw new UnsupportedOperationException();
    }
}

class Exemplar {
    public Exemplar(int tombo, String localizacao, Edicao edicao) {
        throw new UnsupportedOperationException();
    }

    public int getTombo() { throw new UnsupportedOperationException(); }
    public String getLocalizacao() { throw new UnsupportedOperationException(); }
    public Edicao getEdicao() { throw new UnsupportedOperationException(); }
    public boolean isEmprestado() { throw new UnsupportedOperationException(); }
    public void mover(String novaLocalizacao) { throw new UnsupportedOperationException(); }
    public boolean emprestar() { throw new UnsupportedOperationException(); }
    public boolean devolver() { throw new UnsupportedOperationException(); }
}