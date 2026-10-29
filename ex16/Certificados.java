import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

final class Campo {
    final String nome;
    final int tamanho;
    public Campo(String nome, int tamanho) { this.nome = nome; this.tamanho = tamanho; }
}

final class RegistroHistorico {
    private final String acao;
    private final String estadoAnterior;
    private final String estadoPosterior;
    public RegistroHistorico(String acao, String anterior, String posterior) {
        this.acao = acao; this.estadoAnterior = anterior; this.estadoPosterior = posterior;
    }
    public String getAcao() { return acao; }
    public String getEstadoAnterior() { return estadoAnterior; }
    public String getEstadoPosterior() { return estadoPosterior; }
}

class OperacaoInvalida extends RuntimeException {
    public OperacaoInvalida(String mensagem) { super(mensagem); }
}

interface EstadoCertificado {
    String nome();
    default void alterar(Certificado c, String placa) { throw new OperacaoInvalida("Alteracao nao permitida"); }
    default void assinar(Certificado c) { throw new OperacaoInvalida("Assinatura nao permitida"); }
    default void utilizar(Certificado c) { throw new OperacaoInvalida("Utilizacao nao permitida"); }
    default void cancelar(Certificado c) { throw new OperacaoInvalida("Cancelamento nao permitido"); }
    default void suspender(Certificado c) { throw new OperacaoInvalida("Suspensao nao permitida"); }
    default void reativar(Certificado c) { throw new OperacaoInvalida("Reativacao nao permitida"); }
}

class NaoEmitido implements EstadoCertificado {
    public String nome() { return "NAO_EMITIDO"; }
}

class Emitido implements EstadoCertificado {
    public String nome() { return "EMITIDO"; }
}

class Suspenso implements EstadoCertificado {
    public String nome() { return "SUSPENSO"; }
}

class Utilizado implements EstadoCertificado {
    public String nome() { return "UTILIZADO"; }
}

class Cancelado implements EstadoCertificado {
    public String nome() { return "CANCELADO"; }
}

class FabricaEstados {
    public static EstadoCertificado criar(String codigo) {
        if ("N".equals(codigo)) return new NaoEmitido();
        throw new IllegalArgumentException("Codigo de estado desconhecido");
    }
}

class Certificado {
    private String numero;
    private String placa;
    private EstadoCertificado estado;
    private final List<RegistroHistorico> historico = new ArrayList<>();

    public Certificado(String numero, String placa) {
        this.numero = numero; this.placa = placa; this.estado = new NaoEmitido();
    }
    public String getNumero() { return numero; }
    public void setNumero(String numero) { this.numero = numero; }
    public String getPlaca() { return placa; }
    public void setPlaca(String placa) { this.placa = placa; }
    public String getEstado() { return estado.nome(); }
    public void trocarEstado(EstadoCertificado estado) { this.estado = estado; }
    public List<RegistroHistorico> getHistorico() { return List.copyOf(historico); }

    public void alterar(String placa) {
        estado.alterar(this, placa);
    }
    public void assinar() {
        estado.assinar(this);
    }
    public void utilizar() {
        estado.utilizar(this);
    }
    public void cancelar() {
        estado.cancelar(this);
    }
    public void suspender() {
        estado.suspender(this);
    }
    public void reativar() {
        estado.reativar(this);
    }
}

abstract class ParserRegistro<T> {
    protected final Campo[] campos;
    public ParserRegistro() {
        this(new Campo[]{new Campo("numero", 4), new Campo("placa", 7), new Campo("estado", 1)});
    }
    public ParserRegistro(Campo[] campos) { this.campos = campos.clone(); }
    public final T parse(String linha) {
        throw new UnsupportedOperationException();
    }
    protected abstract T criarResultado();
    protected abstract void atribuir(T resultado, String campo, String valor);
}

class ParserMapa extends ParserRegistro<Map<String, String>> {
    public ParserMapa() { super(); }
    public ParserMapa(Campo[] campos) { super(campos); }
    protected Map<String, String> criarResultado() { return new LinkedHashMap<>(); }
    protected void atribuir(Map<String, String> r, String campo, String valor) {
        throw new UnsupportedOperationException();
    }
}

class ParserCertificado extends ParserRegistro<Certificado> {
    public ParserCertificado() { super(); }
    public ParserCertificado(Campo[] campos) { super(campos); }
    protected Certificado criarResultado() { return new Certificado("", ""); }
    protected void atribuir(Certificado r, String campo, String valor) {
        throw new UnsupportedOperationException();
    }
}

public class Certificados {
    public static void main(String[] args) {
        try {
            Certificado c = new ParserCertificado().parse("0042ABC1234E");
            c.suspender();
            try { c.utilizar(); }
            catch (OperacaoInvalida erro) { System.out.println("Utilizacao recusada enquanto suspenso"); }
            c.reativar();
            c.utilizar();
            System.out.println(c.getNumero() + " " + c.getPlaca() + " " + c.getEstado());
            for (RegistroHistorico r : c.getHistorico()) {
                System.out.println(r.getAcao() + " " + r.getEstadoAnterior() + " " + r.getEstadoPosterior());
            }
        } catch (RuntimeException erro) {
            System.out.println(erro.getClass().getSimpleName() + ": " + erro.getMessage());
        }
    }
}
