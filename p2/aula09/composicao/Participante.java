package composicao;

public class Participante {
    private String nome;
    private String email;
    private int idade;
    
    public Participante(String nome, String email, int idade) {
        this.nome = nome;
        this.email = email;
        this.idade = idade;
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
}
