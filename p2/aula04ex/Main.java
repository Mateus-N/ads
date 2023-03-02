package aula04ex;

public class Main {
    public static void main(String[] args) {
        Kart kart = new Kart();
        Piloto mario = new Piloto("Mario", kart);

        mario.acelerarKart(40);
        kart.pegarMoeda(5);
        mario.frear();
        mario.acelerarKart(100);
        mario.reduzVelocidade(40);
        kart.bater();
    }
}
