package encapsulamento;

public class Senha {
    private int valor;

    public int getValor() {
        return valor;
    }
    public void setValor(int valor) {
        if (valor >= 1000 && valor <= 9999) {
            this.valor = valor;
        } else {
            System.out.println("Valor inválido");
        }
    }
}
