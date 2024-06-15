import java.util.Scanner;

public class Pattern2 {
    public static void main(String[] args) {
        int i, j, n;
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter No : ");
        n = scan.nextInt();
        for (i = n; i >= 0; i--) {
            for (j = i; j < n; j++)
                System.out.print(" ");
            for (j = 0; j <= (i - 1); j++)
                System.out.print(" *");
            System.out.println("");
        }
    }
}