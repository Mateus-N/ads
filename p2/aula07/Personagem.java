package aula07;

public class Personagem {
    private String nome;
    private String poder;
    private String objetivo;
    private String nomeReal;

    protected Personagem(String nome, String poder, String objetivo, String nomeReal) {
        this.nome = nome;
        this.poder = poder;
        this.objetivo = objetivo;
        this.nomeReal = nomeReal;
    }

    public String getNome() {
        return nome;
    }
    public String getPoder() {
        return poder;
    }
    public String getObjetivo() {
        return objetivo;
    }
    public String getNomeReal() {
        return nomeReal;
    }

    public void apresentar() {
        System.out.println("Olá, me chamo " + getNome() + " e meu objetivo é " + getObjetivo());
    }

    public void lutar(Personagem perso) {
        System.out.println(getNome() + " está lutando contra " + perso.getNome());
    }
}
