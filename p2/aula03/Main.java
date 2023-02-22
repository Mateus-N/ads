package aula03;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        try (Scanner input = new Scanner(System.in)) {
            System.out.print("Quantas séries deseja adicionar: ");
            int quantidadesSeries = input.nextInt();
            input.nextLine();
            SerieFavorita[] series = new SerieFavorita[quantidadesSeries];
            
            for (int i = 0; i < quantidadesSeries; i++){
                series[i] = new SerieFavorita();
                
                System.out.println("Série " + (i + 1));
                System.out.print("Nome da sua série " + (i + 1) + ": ");
                series[i].setNome(input.nextLine());

                System.out.print("Gênero: ");
                series[i].setGenero(input.nextLine());

                System.out.print("Temporadas: ");
                series[i].setTemporadas(input.nextInt());
                input.nextLine();
            }

            System.out.println("As séries adicionadas foram:");
            for (int i = 0; i < quantidadesSeries; i++){
                System.out.println("A séria favorita é " + series[i].getNome());
                System.out.println("tem como gênero " + series[i].getGenero());
                System.out.println("Tem um total de " + series[i].getTemporadas());
            }
        }
    }
}
