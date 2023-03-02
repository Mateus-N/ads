package aula05;

public class Contato {
    private String email;
    private String numeroDeCelular;

    public String getEmail() {
        return email;
    }
    public void setEmail(String email) {
        this.email = email;
    }
    public String getNumeroDeCelular() {
        return numeroDeCelular;
    }
    public void setNumeroDeCelular(String numeroDeCelular) {
        this.numeroDeCelular = numeroDeCelular;
    }

    public String toString() {
        return "Email: " + email
            + "\nNumero de celular: " + numeroDeCelular;
    }
}
