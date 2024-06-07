import java.util.Arrays;

public class SomaIndex {
    public static int[] somanumeros(int[] array, int somaalvo) {

        Arrays.sort(array);
        int esquerda = 0;
        int direita = array.length - 1;

        while (esquerda < direita) {
            int soma = array[esquerda] + array[direita];

            if (soma == somaalvo) {
                return new int[]{esquerda, direita};
            } else if (soma < somaalvo) {
                esquerda++;
            } else {
                direita--;
            }
        }
        return new int[]{};
    }
}
