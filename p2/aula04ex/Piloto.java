package aula04ex;

public class Piloto {
    private String nome;
    private Kart kart;
    private int pontos;

    public String getNome() {
        return nome;
    }

    public Kart getKart() {
        return kart;
    }
    
    public int getPontos() {
        return pontos;
    }

    public Piloto(String nome, Kart kart) {
        this.nome = nome;
        this.kart = kart;
        kart.setPiloto(this);
    }

    public void imprimirPontos() {
        System.out.println("A quantidade de pontos do piloto " + nome + " é de " + pontos + " pontos");
    }

    public void acelerarKart(int velocidade) {
        System.out.println(nome + " acelerou " + velocidade + " Km/h");
        kart.acelerar(velocidade);
    }

    public void reduzVelocidade(int velocidade) {
        System.out.println(nome + " reduziu " + velocidade + " Km/h");
        kart.reduzVelocidade(velocidade);
    }

    public void frear() {
        kart.frear();
    }

    public void ganhaPontos(int moedas) {
        pontos += moedas * 10;
        imprimirPontos();
    }

    public void perdePontos() {
        pontos /= 2;
        imprimirPontos();
    }
}
