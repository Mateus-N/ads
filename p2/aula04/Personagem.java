package aula04;

public class Personagem {
    private String nome;
    private SerieFavorita serie;

    public SerieFavorita getSerie() {
        return serie;
    }

    public void setSerie(SerieFavorita serie) {
        this.serie = serie;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
}
