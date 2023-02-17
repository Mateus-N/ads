package aula04;

public class Main {
    public static void main(String[] args) {
        SerieFavorita s1 = new SerieFavorita();
        s1.setNome("Supernatural");

        Personagem p1 = new Personagem();
        p1.setNome("Deus");

        s1.setPersonagem(p1);
        p1.setSerie(s1);

        System.out.println(s1.getPersonagem().getNome());
        System.out.println(p1.getSerie().getNome());
    }
}
