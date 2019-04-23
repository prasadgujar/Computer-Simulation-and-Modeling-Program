/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the number of random numbers:");
		int n = sc.nextInt();
		System.out.println("Entered no:"+n);
		double ran[] = new double[n];
		double x[] = new double[n];
		x[0] = 0;
		int a = 22;
		int c = 1;
		int m = 72;
		for(int i=1;i<n;i++)
		{
			x[i] = (a*x[i-1]+c)%m;
			ran[i]=((a*x[i-1]+c)%m)/m;
			ran[i] = Math.floor(ran[i]*100)/100;
		}
		System.out.println("Random numbers are:");
		for(int tt=0;tt<n;tt++)
		{
			System.out.println(ran[tt]);
		}
		boolean s[] =  new boolean[n];
		int ram = 0,rbm=0,b=0;
		double m1=0.495; //mean =m1=0.495
		for(int t=0;t<n;t++)
		{
			if(ran[t]>m1)
			{
				s[t] = false;
				ram++;
			}
			else
			{
				s[t] = true;
				rbm++;
			}
		}
		
		for(int i=0;i<n;i++)
		{
			//System.out.println(s[i]);
		}
		
		for(int k=0;k<n&&(k+1)<n;k++)
		{
			if(s[k]!=s[k+1])
			{
				b++;
				//System.out.println(k);
			}
		}
		++b;
		
		//System.out.println(ram+"rab"+rbm);
		System.out.println("Runs up and down method: \n");
		double mean = ((double)(2*ram*rbm)/(double)n)+0.5;
		double variance =  (double)((2*ram*rbm)*(2*ram*rbm-n))/(double)(n*n*(n-1));
		double z = (b-mean)/Math.sqrt(variance);
		System.out.println("b= "+b+"\n mean:"+ mean+"\nvariance:"+variance+"\n z="+z);
		if(z>=-1.96 && z<=1.96)
		{
			System.out.println("Result: Independent");
		}
		else
		{
			System.out.println("Result: not");
		}
	}
}