import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] numeros = {3 , 2 ,4 , 8 , 10 , 5 , 1};
        int somaalvo = 14;
        System.out.println("Seu numero alvo " + somaalvo  );
        System.out.println("foi encontrado nas posições " + Arrays.toString(SomaIndex.somanumeros(numeros, somaalvo)));
    }
}

