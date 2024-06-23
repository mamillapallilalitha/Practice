import java.util.Scanner;

public class NumbersPattern {

	public static void main(String[] args) {
		int i, j, n, count = 0;
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter No : ");
		n = scan.nextInt();

		for (i = 1; i <= n; i++) {

			for (j = 1; j < i; j++){
				System.out.print(" ");
			}
			count = 0;
			for (j = i; j <= n; j++) {
				count++;
				System.out.print(count);
				System.out.print(" ");
			}
			System.out.println();

		}

		for (i = 1; i < n; i++) {

			for (j = n - 1; j > i; j--){
				System.out.print(" ");
			}
				count = 0;
			for (j = 0; j <= i; j++) {
				count++;
				System.out.print(count);
				System.out.print(" ");
			}
			System.out.println();
		}
	}

}