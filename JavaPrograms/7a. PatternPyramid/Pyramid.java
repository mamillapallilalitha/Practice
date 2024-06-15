import java.util.Scanner;

public class Pyramid {
    public static void main(String[] args) {
        int i,j,n;
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter No : ");
        n = scan.nextInt();
        for (i = 0; i < n; i++) {
            for (j = n - i; j > 1; j--)
                System.out.print(" ");
            for (j = 0; j <= i; j++)
                System.out.print(" *");
            System.out.println();
        }
    }

}