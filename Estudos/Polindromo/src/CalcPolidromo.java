public class CalcPolidromo {
    public static int resultado(int num) {

        int original = num;

        int reverso = 0;


        while (num > 0) {
            int digito = num % 10;
            reverso = reverso * 10 + digito;
            num /= 10;
        }

        if (original == reverso) {
            return original; // Se for um palíndromo, retorna o número original
        } else {
            return -1; // Se não for um palíndromo, retorna -1 (ou outro valor que você preferir)
        }
    }
}