import java.util.Map;

public final class PoliticaEmprestimo {

    private static final Map<String, Map<String, Integer>> PRAZOS =
        Map.of(
            "ALUNO",
            Map.of(
                "LIVRO", 14,
                "REVISTA", 7,
                "MIDIA", 3
            ),

            "PROFESSOR",
            Map.of(
                "LIVRO", 30,
                "REVISTA", 14,
                "MIDIA", 7
            )
        );

    private static final Map<String, Double> TAXAS_MULTA =
        Map.of(
            "LIVRO", 1.0,
            "REVISTA", 1.5,
            "MIDIA", 3.0
        );

    private PoliticaEmprestimo() {
    }

    private static void validarPerfil(String perfil) {
        if (!PRAZOS.containsKey(perfil)) {
            throw new IllegalArgumentException(
                "Perfil inválido"
            );
        }
    }

    private static void validarMaterial(String material) {
        if (!TAXAS_MULTA.containsKey(material)) {
            throw new IllegalArgumentException(
                "Material inválido"
            );
        }
    }

    public static int prazoEmprestimo(
        String perfil,
        String material
    ) {
        validarPerfil(perfil);
        validarMaterial(material);

        return PRAZOS.get(perfil).get(material);
    }

    public static double calcularMulta(
        String material,
        int diasAtraso
    ) {
        validarMaterial(material);

        if (diasAtraso <= 0) {
            return 0.0;
        }

        double taxa = TAXAS_MULTA.get(material);

        int diasNormais =
            Math.min(diasAtraso, 10);

        int diasAgravados =
            Math.max(diasAtraso - 10, 0);

        return diasNormais * taxa
             + diasAgravados * taxa * 2;
    }

    public static boolean podeRenovar(
        String perfil,
        String material,
        int diasAtraso,
        boolean possuiReserva,
        int renovacoesRealizadas
    ) {
        validarPerfil(perfil);
        validarMaterial(material);

        if (renovacoesRealizadas < 0) {
            throw new IllegalArgumentException(
                "Número de renovações inválido"
            );
        }

        if (diasAtraso > 0 || possuiReserva) {
            return false;
        }

        if (material.equals("MIDIA")) {
            return false;
        }

        if (material.equals("REVISTA")) {
            return renovacoesRealizadas < 1;
        }

        int limite =
            perfil.equals("ALUNO") ? 2 : 3;

        return renovacoesRealizadas < limite;
    }
}