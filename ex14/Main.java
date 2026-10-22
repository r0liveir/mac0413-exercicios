// Legado funcional: compare os métodos repetidos nos dois formatos.
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Venda {
    public final String nome;
    public final int quantidade;
    public final long precoCentavos;

    public Venda(String nome, int quantidade, long precoCentavos) {
        this.nome = nome;
        this.quantidade = quantidade;
        this.precoCentavos = precoCentavos;
    }
}

class Resumo {
    public final int quantidade;
    public final long totalCentavos;

    public Resumo(int quantidade, long totalCentavos) {
        this.quantidade = quantidade;
        this.totalCentavos = totalCentavos;
    }
}

class RepositorioVendas {
    private final List<Venda> vendas;

    public RepositorioVendas(List<Venda> vendas) {
        this.vendas = new ArrayList<>(vendas);
    }

    public List<Venda> consultar() {
        return new ArrayList<>(vendas);
    }
}

class ArmazenamentoMemoria {
    private final Map<String, String> arquivos = new HashMap<>();

    public void salvar(String destino, String conteudo) {
        arquivos.put(destino, conteudo);
    }

    public String ler(String destino) {
        return arquivos.get(destino);
    }
}



class RelatorioTexto {
    public String gerar(List<Venda> vendas) {
        Resumo resumo = resumir(vendas);
        return cabecalho() + corpo(vendas) + rodape(resumo);
    }

    protected Resumo resumir(List<Venda> vendas) {
        int quantidade = 0;
        long total = 0;
        for (Venda venda : vendas) {
            quantidade += venda.quantidade;
            total += venda.quantidade * venda.precoCentavos;
        }
        return new Resumo(quantidade, total);
    }

    protected String cabecalho() {
        return "RELATORIO DE VENDAS\n";
    }

    protected String corpo(List<Venda> vendas) {
        StringBuilder texto = new StringBuilder();
        for (Venda v : vendas) {
            texto.append(v.nome).append(" | qtd=").append(v.quantidade)
                 .append(" | unit=").append(v.precoCentavos)
                 .append(" | subtotal=").append(v.quantidade * v.precoCentavos).append('\n');
        }
        return texto.toString();
    }

    protected String rodape(Resumo resumo) {
        return "TOTAL | qtd=" + resumo.quantidade + " | valor=" + resumo.totalCentavos + "\n";
    }
}


class RelatorioCSV {
    public String gerar(List<Venda> vendas) {
        Resumo resumo = resumir(vendas);
        return cabecalho() + corpo(vendas) + rodape(resumo);
    }

    protected Resumo resumir(List<Venda> vendas) {
        int quantidade = 0;
        long total = 0;
        for (Venda venda : vendas) {
            quantidade += venda.quantidade;
            total += venda.quantidade * venda.precoCentavos;
        }
        return new Resumo(quantidade, total);
    }

    protected String cabecalho() {
        return "produto;quantidade;unitario_centavos;subtotal_centavos\n";
    }

    protected String corpo(List<Venda> vendas) {
        StringBuilder texto = new StringBuilder();
        for (Venda v : vendas) {
            texto.append(v.nome).append(';').append(v.quantidade).append(';')
                 .append(v.precoCentavos).append(';')
                 .append(v.quantidade * v.precoCentavos).append('\n');
        }
        return texto.toString();
    }

    protected String rodape(Resumo resumo) {
        return "TOTAL;" + resumo.quantidade + ";;" + resumo.totalCentavos + "\n";
    }
}


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader leitor = new BufferedReader(new InputStreamReader(System.in));
        String formato = leitor.readLine().trim();
        String destino = leitor.readLine().trim();
        int n = Integer.parseInt(leitor.readLine());
        List<Venda> vendas = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String[] partes = leitor.readLine().split(";", -1);
            vendas.add(new Venda(partes[0], Integer.parseInt(partes[1]), Long.parseLong(partes[2])));
        }

        RepositorioVendas repositorio = new RepositorioVendas(vendas);
        ArmazenamentoMemoria armazenamento = new ArmazenamentoMemoria();
        // As classes ainda não têm uma superclasse comum.
        String conteudo;
        if (formato.equals("TEXTO")) {
            conteudo = new RelatorioTexto().gerar(repositorio.consultar());
        } else {
            conteudo = new RelatorioCSV().gerar(repositorio.consultar());
        }
        armazenamento.salvar(destino, conteudo);
        System.out.print(armazenamento.ler(destino));
    }
}