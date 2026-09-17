// ============================================================
// ABSTRAÇÕES DOS PRODUTOS
// NÃO MODIFICAR, POR FAVOR
// ============================================================

interface Veiculo {
    String nome();
    String operar();
}


interface Sensor {
    String nome();
    String coletar();
}


interface Relatorio {
    String gerar(String resumo);
}


// ============================================================
// PRODUTOS CONCRETOS
// NÃO MODIFICAR, POR FAVOR
// ============================================================

class RoverDeserto implements Veiculo {

    @Override
    public String nome() {
        return "RoverDeserto";
    }

    @Override
    public String operar() {
        return "exploracao no deserto";
    }
}


class RoverPolar implements Veiculo {

    @Override
    public String nome() {
        return "RoverPolar";
    }

    @Override
    public String operar() {
        return "exploracao polar";
    }
}


class SensorTermico implements Sensor {

    @Override
    public String nome() {
        return "SensorTermico";
    }

    @Override
    public String coletar() {
        return "temperatura";
    }
}


class SensorGelo implements Sensor {

    @Override
    public String nome() {
        return "SensorGelo";
    }

    @Override
    public String coletar() {
        return "espessura do gelo";
    }
}


class RelatorioTexto implements Relatorio {

    @Override
    public String gerar(String resumo) {
        return "TEXTO: " + resumo;
    }
}


class RelatorioDetalhado implements Relatorio {

    @Override
    public String gerar(String resumo) {
        return "DETALHADO: " + resumo;
    }
}


// ============================================================
// ABSTRACT FACTORY
//
// Define o contrato para criação de uma família completa
// de equipamentos relacionados.
//
// NÃO MODIFICAR ESTA INTERFACE, POR FAVOR.
// ============================================================

interface EquipamentoFactory {

    Veiculo criarVeiculo();

    Sensor criarSensor();
}


// ============================================================
// SUA IMPLEMENTAÇÃO
//
// Complete as duas fábricas concretas.
// ============================================================

class DesertoFactory implements EquipamentoFactory {

    @Override
    public Veiculo criarVeiculo() {
        // TODO: implementar
        return null;
    }

    @Override
    public Sensor criarSensor() {
        // TODO: implementar
        return null;
    }
}


class PolarFactory implements EquipamentoFactory {

    @Override
    public Veiculo criarVeiculo() {
        // TODO: implementar
        return null;
    }

    @Override
    public Sensor criarSensor() {
        // TODO: implementar
        return null;
    }
}


// ============================================================
// FACTORY METHOD
//
// O fluxo geral da missão já está implementado.
// As subclasses decidem qual relatório será criado.
//
// NÃO MODIFICAR executar().
// ============================================================

abstract class Missao {

    public abstract Relatorio criarRelatorio();

    public final String executar(
            Veiculo veiculo,
            Sensor sensor
    ) {

        String resumo =
                veiculo.nome()
                + " | "
                + veiculo.operar()
                + " | "
                + sensor.nome()
                + " | "
                + sensor.coletar();

        Relatorio relatorio =
                criarRelatorio();

        return relatorio.gerar(resumo);
    }
}


// ============================================================
// SUA IMPLEMENTAÇÃO
//
// Complete o Factory Method das duas subclasses.
// ============================================================

class MissaoRapida extends Missao {

    @Override
    public Relatorio criarRelatorio() {
        // TODO: implementar
        return null;
    }
}


class MissaoCientifica extends Missao {

    @Override
    public Relatorio criarRelatorio() {
        // TODO: implementar
        return null;
    }
}


// ============================================================
// INTEGRAÇÃO
//
// O planejador deve trabalhar apenas com as abstrações
// Missao e EquipamentoFactory.
// ============================================================

class PlanejadorMissoes {

    public String executarMissao(
            Missao missao,
            EquipamentoFactory fabrica
    ) {

        // TODO:
        // 1. solicitar um veículo à fábrica;
        // 2. solicitar um sensor à fábrica;
        // 3. executar a missão com os objetos criados;
        // 4. retornar o resultado da execução.

        return null;
    }
}


// ============================================================
// Essa classe pública é necessária para a entrega como Atividade.java.
//
// Não é necessário implementar main.
// ============================================================

public class Atividade {
}