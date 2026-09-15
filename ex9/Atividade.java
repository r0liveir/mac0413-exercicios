import java.util.ArrayList;
import java.util.List;


// ============================================================
// EXCEÇÕES
// POR FAVOR, NÃO MODIFICAR
// ============================================================

class SensorIndisponivelException extends RuntimeException {

    public SensorIndisponivelException(String mensagem) {
        super(mensagem);
    }
}


class MedidorJaRegistradoException extends RuntimeException {

    public MedidorJaRegistradoException(String mensagem) {
        super(mensagem);
    }
}


class MedidorNaoEncontradoException extends RuntimeException {

    public MedidorNaoEncontradoException(String mensagem) {
        super(mensagem);
    }
}


// ============================================================
// CONTRATO UTILIZADO PELA ESTAÇÃO
// POR FAVOR, NÃO MODIFICAR
// ============================================================

interface Medidor {

    String getId();

    double medir();
}


// ============================================================
// COMPONENTES EXTERNOS
// POR FAVOR, NÃO MODIFICAR
// ============================================================

class TermometroAntigo {

    private final String codigo;
    private final double temperaturaFahrenheit;

    public TermometroAntigo(
            String codigo,
            double temperaturaFahrenheit
    ) {
        this.codigo = codigo;
        this.temperaturaFahrenheit = temperaturaFahrenheit;
    }

    public String codigo() {
        return codigo;
    }

    public double lerFahrenheit() {
        return temperaturaFahrenheit;
    }
}


class SensorDigital {

    private final String serial;
    private final double temperaturaCelsius;
    private final boolean operacional;

    public SensorDigital(
            String serial,
            double temperaturaCelsius,
            boolean operacional
    ) {
        this.serial = serial;
        this.temperaturaCelsius = temperaturaCelsius;
        this.operacional = operacional;
    }

    public String serial() {
        return serial;
    }

    public boolean estaOperacional() {
        return operacional;
    }

    public double obterLeitura(String unidade) {

        if (!"C".equals(unidade)) {
            throw new IllegalArgumentException(
                    "Unidade não suportada"
            );
        }

        return temperaturaCelsius;
    }
}


// ============================================================
// A PARTIR DAQUI É SUA IMPLEMENTAÇÃO...
// ============================================================

class TermometroAdapter implements Medidor {

    private final TermometroAntigo termometro;

    public TermometroAdapter(TermometroAntigo termometro) {
        this.termometro = termometro;
    }

    @Override
    public String getId() {
        return null;
    }

    @Override
    public double medir() {
        return 0.0;
    }
}


class SensorDigitalAdapter implements Medidor {

    private final SensorDigital sensor;

    public SensorDigitalAdapter(SensorDigital sensor) {
        this.sensor = sensor;
    }

    @Override
    public String getId() {
        return null;
    }

    @Override
    public double medir() {
        return 0.0;
    }
}


class CentralMonitoramento {

    private CentralMonitoramento() {
    }

    public static CentralMonitoramento getInstance() {
        return null;
    }

    public void registrar(Medidor medidor) {
    }

    public boolean remover(String identificador) {
        return false;
    }

    public int quantidade() {
        return 0;
    }

    public double medir(String identificador) {
        return 0.0;
    }

    public double temperaturaMedia() {
        return 0.0;
    }

    public List<String> sensoresEmAlerta(double limite) {
        return new ArrayList<>();
    }
}


// Classe mantida apenas para permitir a entrega como Atividade.java.
// Não é necessário implementar main.
public class Atividade {
}