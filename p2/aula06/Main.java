package aula06;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Encontro encontro = new Encontro();
        Agenda agenda = new Agenda();

        System.out.print("Quantos encontros deseja adicionar? ");
        int quantos = input.nextInt();
        input.nextLine();

        for (int i = 0; i < quantos; i++) {
            boolean pedeMes = true;
            while (pedeMes) {
                System.out.print("Digite um mes: ");
                encontro.setMes(input.nextInt());
                input.nextLine();
                if (encontro.getMes() != 0) {
                    pedeMes = false;
                }
            }
            
            boolean pedeDia = true;
            while (pedeDia) {
                System.out.print("Digite um dia: ");
                encontro.setDia(input.nextInt());
                input.nextLine();
                if (encontro.getDia() != 0) {
                    pedeDia = false;
                }
            }

            System.out.print("Digite a descrição: ");
            encontro.setDescricao(input.nextLine());
        }
        agenda.addEncontros(encontro);

        agenda.imprimirEncontros();
    }
}
