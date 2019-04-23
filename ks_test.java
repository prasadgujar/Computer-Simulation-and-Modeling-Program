/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
		int a,c,m,n;
		double dmmax=0,dpmax=0,d;
		
		Scanner in = new Scanner(System.in);
		System.out.println("enter the number of random numbers");
		n = in.nextInt();
		double[] x = new double[n];
		double[] dp = new double[n];
		double[] dm = new double[n];
		
		a = 5;
		c = 10;
		m = 15;
		x[0] = 0.1;
		System.out.println("\n random numbers are:\n \t");
		System.out.println(""+x[0]);
		for(int i=1;i<n;i++)
		{
			x[i] = ((a*x[i-1]+c)%m)/m;
			x[i] = (double)Math.floor(x[i]*100)/100;
			System.out.print(" "+x[i]);
			
		}
		Arrays.sort(x);
		System.out.println("\n \n Sorted random numbers are: \n \t");
		for(int k=0;k<n;k++)
		{
			System.out.println(x[k]+" ");
		}
		for(int j=0;j<n;j++)
		{
			dp[j] = ((double)(j+1)/n)-x[j];
			dm[j] = x[j] -((double)j/n);
			if(dpmax <dp[j])
			{
				dpmax = dp[j];
			}
			else
			{
				dmmax = dm[j];
			}
			System.out.println(" \n\n For random number "+(j+1)+": \n \t dp = "+dp[j]+"dm = "+dm[j]);
		}
		
		if(dpmax>dmmax)
		{
			d = dpmax;
		}
		else
		{
			d = dmmax;
		}
		
		System.out.println("\n value of d="+d);
		
		if(d<0.565)
		{
			System.out.println("Numbers are uniformily generated.");
		}
		else
		{
			System.out.println("Numbers are not uniformily generated.");
		}
	}
}