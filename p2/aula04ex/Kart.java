package aula04ex;

public class Kart {
    private int velocidade;
    private Piloto piloto;

    public double getVelocidade() {
        return velocidade;
    }
    public Piloto getPiloto() {
        return piloto;
    }
    public void setPiloto(Piloto piloto) {
        this.piloto = piloto;
    }

    public void getVelocidadeEmString(){
        System.out.println("A velocidade do kart do piloto " + piloto.getNome() + " é de " + velocidade + " Km/h");
    }

    public void acelerar(int velocidade) {
        this.velocidade += velocidade;
        getVelocidadeEmString();
    }

    public void reduzVelocidade(int velocidade) {
        this.velocidade -= velocidade;
        getVelocidadeEmString();
    }

    public void frear() {
        velocidade = 0;
        System.out.println("Freio ativado");
        getVelocidadeEmString();
    }

    public void bater() {
        System.out.println("Kart bateu, perdeu metade da velocidade e " +
            piloto.getNome() + " perdeu metade dos pontos");
        velocidade /= 2;
        piloto.perdePontos();
        getVelocidadeEmString();
    }

    public void pegarMoeda(int moedas) {
        System.out.println("Pegou " + moedas + " moedas");
        piloto.ganhaPontos(moedas);
    }
}
