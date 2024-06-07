import java.util.Scanner;

public class CalculoSoma {
   public static int somatotal(int num){
      if (num == 0) {
         return 0;
      }
      while (num >= 10){
         int soma = 0;
         while (num > 0) {
            soma += num % 10;
            num /= 10;
         }
         num = soma;
      }
      return num;
   }

}
