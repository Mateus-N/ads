package encapsulamento;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        try (Scanner in = new Scanner(System.in)) {
            Senha senha = new Senha();
            senha.setValor(1234);

            System.out.print("Digite a senha: ");
            int digitado = Integer.parseInt(in.nextLine());

            if (senha.getValor() == digitado) {
                System.out.println("Acesso permitido");
            } else {
                System.out.println("Acesso negado");
            }
        } catch (NumberFormatException e) {
            e.printStackTrace();
        }
    }
}