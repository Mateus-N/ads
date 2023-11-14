package br.edu.unifip;

public class Aluno {
    private String nome;
    private String email;
    private int idade;
    private double media;

    public Aluno(String nome, String email, int idade, double media) {
        this.nome = nome;
        this.email = email;
        this.idade = idade;
        this.media = media;
    }

    public String getNome() {
        return nome;
    }

    public String getEmail() {
        return email;
    }

    public int getIdade() {
        return idade;
    }

    public double getMedia() {
        return media;
    }
}
