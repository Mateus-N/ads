package composicao;

public class Organizador {
    private String nome;
    private String email;
    
    public Organizador(String nome, String email) {
        this.nome = nome;
        this.email = email;
    }
    
    public String getNome() {
        return nome;
    }
    public String getEmail() {
        return email;
    }
}
