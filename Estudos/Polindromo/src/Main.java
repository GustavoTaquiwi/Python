import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner leitor = new Scanner(System.in);
        System.out.println("Digite um valor numerico?");
        int valor = leitor.nextInt();
        int result = CalcPolidromo.resultado(valor);
        if (result != -1) {
            System.out.println("O número " + valor + " é um palíndromo.");
        } else {
            System.out.println("O número " + valor + " não é um palíndromo.");
        }
    }
}