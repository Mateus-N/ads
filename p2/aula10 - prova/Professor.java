public class Professor extends Pessoa {
    private String cpf;

    public Professor(String nome, String cpf) {
        super(nome);
        this.cpf = cpf;
    }
    
    public String getCpf() {
        return cpf;
    }
}
