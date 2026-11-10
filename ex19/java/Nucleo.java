public final class Nucleo {
    public interface Repositorio {
        boolean equipamentoExiste(String equipamento);
        boolean equipamentoOcupado(String equipamento);
        boolean alunoTemEmprestimo(String aluno);
        void registrar(String aluno, String equipamento);
    }

    public static class RealizarEmprestimo {
        private final Repositorio repositorio;

        public RealizarEmprestimo(Repositorio repositorio) {
            this.repositorio = repositorio;
        }

        public String executar(String aluno, String equipamento) {
            throw new UnsupportedOperationException();
        }
    }
}
