package aula07;

public class Main {
    public static void main(String[] args) {
        SuperHeroi heroi = new SuperHeroi(
            "Homem-Aranha",
            "Habilidades de aranha",
            "Proteger o povo da minha cidade",
            "Peter Parker"
        );
        Vilao vilao = new Vilao(
            "Duende Verde",
            "Super força",
            "Se tornar o homem mais poderoso do mundo",
            "Norman Osborn"
        );

        heroi.apresentar();
        vilao.apresentar();

        heroi.lutar(vilao);
        vilao.lutar(heroi);
    }
}
