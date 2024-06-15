import java.util.Scanner;
public class Diamond {

    public static void main(String[] args) {
        int i,j,n;
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter No : ");
		n=scan.nextInt();
		 for (i=0; i<n; i++){ 
             for (j=n; j>i+1; j--)             // prints space
               System.out.print(" "); 
             for (j=0; j<=i; j++)             // prints stars with space
               System.out.print(" *"); 
          System.out.println(); 
      } 
	    for(i=n;i>=0;i--)     
		   {
		       System.out.print(" ");
		      for(j=i;j<n;j++)  
		         System.out.print(" ");
		      for(j=0;j<i-1;j++)     
		         System.out.print(" *");    
		      System.out.println();   
		   }
	 }
}
