package aula05;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        try (Scanner input = new Scanner(System.in)) {
            Endereco endereco = new Endereco();
            Contato contado = new Contato();

            System.out.print("Digite seu nome: ");
            String nome = input.nextLine();
            Pessoa pessoa = new Pessoa(nome, endereco, contado);

            System.out.print("Logradouro: ");
            endereco.setLogradouro(input.nextLine());

            System.out.print("Numero da casa: ");
            endereco.setNumero(input.nextInt());
            input.nextLine();

            System.out.print("Bairro: ");
            endereco.setBairro(input.nextLine());

            System.out.print("Cidade: ");
            endereco.setCidade(input.nextLine());

            System.out.print("UF: ");
            endereco.setUf(input.nextLine());

            System.out.print("Email: ");
            contado.setEmail(input.nextLine());

            System.out.print("Numero de celular: ");
            contado.setNumeroDeCelular(input.nextLine());

            pessoa.imprimirDados();
        }
    }
}
