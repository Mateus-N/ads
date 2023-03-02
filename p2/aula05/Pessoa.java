package aula05;

public class Pessoa {
    private String nome;
    private Contato contato;
    private Endereco endereco;

    public String getNome() {
        return nome;
    }
    public Contato getContato() {
        return contato;
    }
    public Endereco getEndereco() {
        return endereco;
    }

    public Pessoa(String nome, Endereco endereco, Contato contato) {
        this.nome = nome;
        this.endereco = endereco;
        this.contato = contato;
    }

    public void imprimirDados() {
        System.out.println("\nNome: " + nome);
        System.out.println(endereco.toString());
        System.out.println(contato.toString());
    }
}
