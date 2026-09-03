import java.io.*;
import java.net.Socket;
import java.util.HashMap;
import java.util.Map;
import java.nio.charset.StandardCharsets;

public class CentralHermes {

    /**
     * Processa uma sessão do protocolo HERMES.
     *
     * IMPORTANTE:
     * - não feche entrada nem saida neste método;
     * - IOException deve ser propagada.
     */
    public static void processar(
            InputStream entrada,
            OutputStream saida
    ) throws IOException {
		Map<String, String> mensagens = new HashMap<>();

		BufferedReader reader = new BufferedReader(new InputStreamReader(entrada, StandardCharsets.UTF_8));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(saida, StandardCharsets.UTF_8));

		String line;
		while ((line = reader.readLine()) != null) {
			if (line.isEmpty()) {
				writer.write("ERRO;FORMATO\n");
                writer.flush();
				continue;
			}
			
			String[] tokens = line.split(";", -1);
			String command = tokens[0];

			switch (command) {
				case "MSG":
					if (tokens.length == 3 && !tokens[1].isEmpty() && !tokens[2].isEmpty()) {
						String id = tokens[1];
						String texto = tokens[2];
						if (mensagens.containsKey(id)) {
							writer.write("ERRO;" + id + ";JA_EXISTE\n");
						} else {
							mensagens.put(id, texto);
							writer.write("OK;" + id + "\n");
						}

					} else {
						writer.write("ERRO;FORMATO\n");
					}
					break;
				case "GET":
					if (tokens.length == 2 && !tokens[1].isEmpty()) {
						String id = tokens[1];
						String texto = mensagens.get(id);
						if (texto != null) {
							writer.write("MSG;" + id + ";" + texto + "\n");
						} else {
							writer.write("ERRO;" + id + ";NAO_ENCONTRADA\n");
						}
					} else {
						writer.write("ERRO;FORMATO\n");
					}
					break;

				case "DEL":
					if (tokens.length == 2 && !tokens[1].isEmpty()) {
						String id = tokens[1];
						String rem = mensagens.remove(id);
						if (rem != null) {
							writer.write("OK;" + tokens[1] + "\n");
						} else {
							writer.write("ERRO;" + tokens[1] + ";NAO_ENCONTRADA\n");
						}
					} else {
						writer.write("ERRO;FORMATO\n");
					}

					break;

				case "COUNT":
					if (tokens.length == 1) {
						writer.write("COUNT;" + mensagens.size() + "\n");
					} else {
						writer.write("ERRO;FORMATO\n");
					}
					break;

				case "FIM":
					if (tokens.length == 1) {
						writer.write("FIM;" + mensagens.size() + "\n");
						writer.flush();
						return;
					} else {
						writer.write("ERRO;FORMATO\n");
					}
					break;
				default:
					writer.write("ERRO;COMANDO\n");
					break;
				
			}
			writer.flush();
		}
    }

    /**
     * Abre os arquivos, reutiliza processar(...) e fecha
     * corretamente os recursos abertos por este método.
     */
    public static void processarArquivo(
            String arquivoEntrada,
            String arquivoSaida
    ) throws IOException {
		InputStream entrada = null;
		OutputStream saida = null;

		try {
			entrada = new FileInputStream(arquivoEntrada);
			saida = new FileOutputStream(arquivoSaida);
			processar(entrada, saida);
		} finally {
			if (entrada != null) {
				entrada.close();
			}
			if (saida != null) {
				saida.close();
			}
		}
    }

    /**
     * Obtém os streams do socket e reutiliza processar(...).
     *
     * Não é necessário fechar o Socket neste método.
     */
    public static void processarCliente(
            Socket cliente
    ) throws IOException {
		InputStream entrada = cliente.getInputStream();
		OutputStream saida = cliente.getOutputStream();

		processar(entrada, saida);
    }
}

