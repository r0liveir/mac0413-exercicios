import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
import java.util.Map;


interface EstadoRobo {

    int atacar(Robo robo);

    void receberDano(Robo robo, int pontos);

    void reparar(Robo robo, int pontos);

    String nome();
}


class EstadoNormal implements EstadoRobo {

    public int atacar(Robo robo) {
        // TODO
        throw new UnsupportedOperationException();
    }

    public void receberDano(Robo robo, int pontos) {
        // TODO
        throw new UnsupportedOperationException();
    }

    public void reparar(Robo robo, int pontos) {
        // TODO
        throw new UnsupportedOperationException();
    }

    public String nome() {
        return "NORMAL";
    }
}


class EstadoCritico implements EstadoRobo {

    public int atacar(Robo robo) {
        // TODO
        throw new UnsupportedOperationException();
    }

    public void receberDano(Robo robo, int pontos) {
        // TODO
        throw new UnsupportedOperationException();
    }

    public void reparar(Robo robo, int pontos) {
        // TODO
        throw new UnsupportedOperationException();
    }

    public String nome() {
        return "CRITICO";
    }
}


class EstadoDesativado implements EstadoRobo {

    public int atacar(Robo robo) {
        // TODO
        throw new UnsupportedOperationException();
    }

    public void receberDano(Robo robo, int pontos) {
        // TODO
        throw new UnsupportedOperationException();
    }

    public void reparar(Robo robo, int pontos) {
        // TODO
        throw new UnsupportedOperationException();
    }

    public String nome() {
        return "DESATIVADO";
    }
}


class Robo {

    private String modelo;
    private int vidaMaxima;
    private int vidaAtual;
    private int ataqueBase;
    private List<String> modulos;
    private EstadoRobo estado;

    public Robo(
            String modelo,
            int vidaMaxima,
            int ataqueBase,
            List<String> modulos
    ) {
        this.modelo = modelo;
        this.vidaMaxima = vidaMaxima;
        this.vidaAtual = vidaMaxima;
        this.ataqueBase = ataqueBase;
        this.modulos = new ArrayList<>(modulos);
        this.estado = new EstadoNormal();
    }

    public int atacar() {
        // TODO: delegar ao estado atual
        throw new UnsupportedOperationException();
    }

    public void receberDano(int pontos) {
        // TODO: delegar ao estado atual
        throw new UnsupportedOperationException();
    }

    public void reparar(int pontos) {
        // TODO: delegar ao estado atual
        throw new UnsupportedOperationException();
    }

    public Robo clonar() {
        // TODO: implementar Prototype
        throw new UnsupportedOperationException();
    }

    public void mudarEstado(EstadoRobo novoEstado) {
        this.estado = novoEstado;
    }

    void reduzirVida(int pontos) {
        if (pontos > 0) {
            vidaAtual = Math.max(0, vidaAtual - pontos);
        }
    }

    void aumentarVida(int pontos) {
        if (pontos > 0) {
            vidaAtual = Math.min(
                    vidaMaxima,
                    vidaAtual + pontos
            );
        }
    }

    public void adicionarModulo(String modulo) {
        modulos.add(modulo);
    }

    public String getModelo() {
        return modelo;
    }

    public int getVidaMaxima() {
        return vidaMaxima;
    }

    public int getVidaAtual() {
        return vidaAtual;
    }

    public int getAtaqueBase() {
        return ataqueBase;
    }

    public List<String> getModulos() {
        return modulos;
    }

    public String getEstado() {
        return estado.nome();
    }
}


class CatalogoRobos {

    private Map<String, Robo> prototipos = new HashMap<>();

    public void registrar(String nome, Robo prototipo) {
        prototipos.put(nome, prototipo);
    }

    public Robo criar(String nome) {
        // TODO: localizar o prototipo e clona-lo
        throw new UnsupportedOperationException();
    }
}


public class Atividade {
    // Nao e necessario implementar main.
}