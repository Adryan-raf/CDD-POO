package Advanced;

import java.util.Scanner;

public class OpEx4 {
	public static void main(String []args) {
		Scanner input= new Scanner(System.in);
		
		int[] a = new int[10], b = new int[10], c = new int[10], d = new int[10];
		
		for(int i=0;i<10;i++) {
			System.out.printf("\nEnter the %d number of first array.\n", i );
			a[i]= input.nextInt();
		}
		for(int i=0;i<10;i++) {
			System.out.printf("\nEnter the %d number of second array.\n", i );
			b[i]= input.nextInt();
		}
		for(int i=0;i<10;i++) {
			System.out.printf("\nEnter the %d number of third array.\n", i );
			c[i]= input.nextInt();
		}
		for(int i=0;i<10;i++) {
			System.out.printf("\nEnter the %d number of fourth array.\n", i );
			d[i]= input.nextInt();
		}
		
		System.out.printf("a)");
		for(int i=0;i<10;i++) {
			System.out.printf("%d ", a[i]);
		}
		System.out.printf("\nb)");
		for(int i=0;i<10;i++) {
			System.out.printf("%d ", b[i]);
		}
		System.out.printf("\nc)");
		for(int i=0;i<10;i++) {
			System.out.printf("%d ", c[i]);
		}
		System.out.printf("\nd)");
		for(int i=0;i<10;i++) {
			System.out.printf("%d ", d[i]);
		}
	}
}
