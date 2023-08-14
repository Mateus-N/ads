package composicao;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        try (Scanner in = new Scanner(System.in)) {
            Evento evento = new Evento();
            evento.setNome("ir à pizzaria");
            evento.setData("15/03/2023");
            evento.setHora("21:30");
            evento.setLocal(new Local("HotPizza", "Rua tal", 50));
            evento.setOrganizador(new Organizador("Mateus", "mateus@email.com"));
            
            System.out.println("Quantos participantes deseja adicionar ao evento " + evento.getNome());
            int quantidade = Integer.parseInt(in.nextLine());

            for (int i = 1; i <= quantidade; i++) {
                System.out.println("Participante " + i);
                System.out.print("Nome: ");
                String nome = in.nextLine();
                System.out.print("Email: ");
                String email = in.nextLine();
                System.out.print("Idade: ");
                int idade = Integer.parseInt(in.nextLine());

                evento.adicionarParticipante(new Participante(nome, email, idade));
            }

            evento.imprimirListaDeParticipantes();
        } catch (NumberFormatException e) {
            e.printStackTrace();
        }
    }
}
