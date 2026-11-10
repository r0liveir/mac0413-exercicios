import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class Emprestimos {
    static class SistemaEmprestimos {
        private final Set<String> equipamentos = Set.of("MIC1", "CAM1", "TRI1");
        private final Map<String, String> emprestimos = new HashMap<>();

        String realizar(String aluno, String equipamento) {
            if (!equipamentos.contains(equipamento)) {
                return "INEXISTENTE";
            }
            if (emprestimos.containsKey(equipamento)) {
                return "INDISPONIVEL";
            }
            if (emprestimos.containsValue(aluno)) {
                return "LIMITE_ALUNO";
            }
            emprestimos.put(equipamento, aluno);
            return "APROVADO";
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader entrada = new BufferedReader(new InputStreamReader(System.in));
        SistemaEmprestimos sistema = new SistemaEmprestimos();
        String linha;
        while ((linha = entrada.readLine()) != null) {
            linha = linha.replaceAll("^[ \\t]+|[ \\t]+$", "");
            if (linha.isEmpty()) {
                continue;
            }
            String[] partes = linha.split("[ \\t]+");
            if (partes.length != 3 || !partes[0].equals("EMPRESTAR")) {
                System.out.println("COMANDO_INVALIDO");
                continue;
            }
            System.out.println(sistema.realizar(partes[1], partes[2]));
        }
    }
}
