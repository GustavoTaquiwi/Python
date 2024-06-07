import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner leitor = new Scanner(System.in);
        System.out.println("Digite um valor Numeiroc Inteiro? ");
        int valor = leitor.nextInt();
        int resultado = CalculoSoma.somatotal(valor);
         System.out.println("Saida "+resultado);
    }
}
