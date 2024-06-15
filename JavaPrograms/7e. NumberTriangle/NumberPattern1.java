import java.util.Scanner;
public class NumberPattern1 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int i,j,n, count=0;
		System.out.print("Enter No : ");
		n = scan.nextInt();
		
		
		for (i = 1; i <= n; i++) {
			for (j = n ; j > i; j--) {
			
			    System.out.print(" ");
			}
			count = 0;
			
			for (j = 1; j <= i; j++) {
				count++;
				System.out.print(count);
				System.out.print(" ");
			}
			System.out.println();
		}
	}

}