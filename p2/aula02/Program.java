public class Program {
    public static void main(String[] args) {
        Carro carro1 = new Carro();
        carro1.ano = 2015;
        carro1.cor = "Branco";

        System.out.println(carro1.ano + " " + carro1.cor);

        Pessoa pessoa1 = new Pessoa();

        pessoa1.idade = 22;
        pessoa1.nome = "Mateus Nunes";

        System.out.println("Nome: " + pessoa1.nome);
        System.out.println("Idade: " + pessoa1.idade);
    }
}
