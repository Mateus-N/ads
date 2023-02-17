package aula01;

public class Program{
    public static void main(String[] args) {
        System.out.println("Salve");
        int idade = 16;
        if (idade >= 18) {
            System.out.println("Maior de idade");
        } else {
            System.out.println("Menor de idade");
            int falta = 18 - idade;
            System.out.println("Faltam " + falta + " anos para vocês ficar de maior");
        }

        //for (int i = 1; i <= 10; i++){
            //System.out.println("5 x " + i + " = " + 5 * i);
        //}

        int i = 1;
        while (i <= 10){
            System.out.println("5 x " + i + " = " + 5 * i);
            i++;
        }
    }
}