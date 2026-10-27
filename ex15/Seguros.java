import java.util.Collection;
import java.util.HashSet;
import java.util.Set;

interface ConsultaCredito {
    boolean consultar(String cliente);
}

interface AvaliacaoRisco {
    boolean avaliar(int valor);
}

interface EmissaoApolice {
    String emitir(String proposta);
}

class HistoricoCredito implements ConsultaCredito {
    private final Set<String> bloqueados;

    public HistoricoCredito(Collection<String> bloqueados) {
        this.bloqueados = new HashSet<>(bloqueados);
    }

    public boolean consultar(String cliente) {
        return !bloqueados.contains(cliente);
    }
}

class AvaliadorRisco implements AvaliacaoRisco {
    private final int limite;

    public AvaliadorRisco(int limite) {
        this.limite = limite;
    }

    public boolean avaliar(int valor) {
        return valor <= limite;
    }
}

class EmissorApolice implements EmissaoApolice {
    private final String prefixo;

    public EmissorApolice(String prefixo) {
        this.prefixo = prefixo;
    }

    public String emitir(String proposta) {
        return prefixo + proposta;
    }

    public String aprovar(String proposta, String cliente, int valor) {
        HistoricoCredito credito = new HistoricoCredito(Set.of("BLOQUEADO"));
        AvaliadorRisco risco = new AvaliadorRisco(1000);
        if (!credito.consultar(cliente)) return "RECUSADA:CREDITO";
        if (!risco.avaliar(valor)) return "RECUSADA:RISCO";
        return "APROVADA:" + emitir(proposta);
    }
}

class MediadorSeguros {
    private final EmissorApolice emissor;

    public MediadorSeguros(ConsultaCredito credito, AvaliacaoRisco risco,
                          EmissaoApolice emissor) {
        this.emissor = new EmissorApolice("AP-");
    }

    public String processar(String proposta, String cliente, int valor) {
        return emissor.aprovar(proposta, cliente, valor);
    }
}

public class Seguros {
    public static void main(String[] args) {
        MediadorSeguros m = new MediadorSeguros(
            new HistoricoCredito(Set.of("BLOQUEADO")),
            new AvaliadorRisco(1000), new EmissorApolice("AP-"));
        System.out.println(m.processar("P1", "ANA", 500));
        System.out.println(m.processar("P2", "BLOQUEADO", 500));
        System.out.println(m.processar("P3", "ANA", 1500));
    }
}