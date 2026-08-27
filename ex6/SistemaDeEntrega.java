import java.util.List;

enum TipoEntrega {
    PADRAO,
    EXPRESSA,
    REFRIGERADA
}

class Entrega {

    private final String codigo;
    private final TipoEntrega tipo;
    private final double distanciaKm;
    private final double horasRefrigeracao;

    public Entrega(
            String codigo,
            TipoEntrega tipo,
            double distanciaKm,
            double horasRefrigeracao) {

        this.codigo = codigo;
        this.tipo = tipo;
        this.distanciaKm = distanciaKm;
        this.horasRefrigeracao = horasRefrigeracao;
    }

    public String getCodigo() {
        return codigo;
    }

    public double calcularCusto() {
        switch (tipo) {
            case PADRAO:
                return 8.00 + 1.50 * distanciaKm;

            case EXPRESSA:
                return 12.00 + 2.50 * distanciaKm;

            case REFRIGERADA:
                return 10.00
                        + 1.80 * distanciaKm
                        + 5.00 * horasRefrigeracao;

            default:
                throw new IllegalStateException("Tipo de entrega desconhecido");
        }
    }
}

class Faturamento {

    public double calcularTotal(List<Entrega> entregas) {
        double total = 0.0;

        for (Entrega entrega : entregas) {
            total += entrega.calcularCusto();
        }

        return total;
    }
}