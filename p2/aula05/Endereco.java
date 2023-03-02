package aula05;

public class Endereco {
    private String logradouro;
    private int numero;
    private String bairro;
    private String cidade;
    private String uf;

    public String getLogradouro() {
        return logradouro;
    }
    public void setLogradouro(String logradouro) {
        this.logradouro = logradouro;
    }
    public int getNumero() {
        return numero;
    }
    public void setNumero(int numero) {
        this.numero = numero;
    }
    public String getBairro() {
        return bairro;
    }
    public void setBairro(String bairro) {
        this.bairro = bairro;
    }
    public String getCidade() {
        return cidade;
    }
    public void setCidade(String cidade) {
        this.cidade = cidade;
    }
    public String getUf() {
        return uf;
    }
    public void setUf(String uf) {
        this.uf = uf;
    }

    public String toString() {
        return "Logradouro: " + logradouro + ", N° " + numero
            + "\nBairro: " + bairro
            + "\nCidade: " + cidade
            + "\nEstado: " + uf;
    }
}
