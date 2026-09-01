class EstoqueInsuficienteException extends Exception {

}


class SaldoInsuficienteException extends Exception {

}


class Estoque {

    private int quantidade;

    public Estoque(int quantidadeInicial) {
        // TODO
    }

    public void reservar(int quantidade) {
        // TODO
    }

    public void devolver(int quantidade) {
        // TODO
    }

    public int getQuantidade() {
        // TODO
        return 0;
    }
}


class Carteira {

    private int saldo;

    public Carteira(int saldoInicial) {
        // TODO
    }

    public void cobrar(int valor) {
        // TODO
    }

    public int getSaldo() {
        // TODO
        return 0;
    }
}


class ProcessadorPedido {

    public static String processar(
        Estoque estoque,
        Carteira carteira,
        int quantidade,
        int precoUnitario
    ) {
        // TODO
        return "";
    }
}