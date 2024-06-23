public class BreakContinue {
  public static void main(String[] args) {
    int i = 0;
    while (i < 10) {
      if (i == 4) {
        i++;
        continue;               //if breka the loop ends at 4.
      }
      System.out.println(i);
      i++;
    }  
  }
}
