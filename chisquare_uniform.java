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
		int i;
		double[] x = new double[6];
		x[0] = 0.05;
		double a;
		Random rd = new Random();
		double rand[] = new double[100];
		System.out.print("Enter alpha: ");
		double alpha = sc.nextDouble();
		double xalpha = 0;
		if(alpha==0.005)
		{
			xalpha = 23.6;
		}
		else if(alpha==0.01)
		{
			xalpha = 21.7;
		}
		else if(alpha == 0.025)
		{
			xalpha = 19.0;
		}
		else if(alpha==0.05)
		{
			xalpha = 16.9;
		}
		else if(alpha==0.01)
		{
			xalpha = 14.7;
		}
		else
		{
			System.out.println("invalid alpha");
			System.exit(0);
		}
		for(i=0;i<100;i++)
		{
			rand[i] = rd.nextInt(100)*1.0/100;
		}
		
		
		int freq[] = new int[10];
		for(i=0;i<10;i++)
		{
			freq[i] = 0;
		}
		
		for(i=0;i<100;i++)
		{
			a = rand[i];
			if(a<=0.1)
			{
				freq[0]++;
			}
			else if(a<=0.2)
			{
				freq[1]++;
			}
			else if(a<=0.3)
			{
				freq[2]++;
			}
			else if(a<=0.4)
			{
				freq[3]++;
			}
			else if(a<=0.5)
			{
				freq[4]++;
			}
			else if(a<=0.6)
			{
				freq[5]++;
			}
			else if(a<=0.7)
			{
				freq[6]++;
			}
			else if(a<=0.8)
			{
				freq[7]++;
			}
			else if(a<=0.9)
			{
				freq[8]++;
			}
			else 
			{
				freq[9]++;
			}
		}
		
		int ei = 10;
		double x1=0;
		System.out.println("\n class\t Frequency\tx");
		for(i=0;i<10;i++)
		{
			System.out.println(i+1+"\t"+freq[i]+"\t\t"+Math.pow(freq[i]-ei,2)/ei);
			x1 +=Math.pow(freq[i]-ei,2)/ei;
		}
		System.out.println("X0_alpha="+xalpha);
		System.out.println("X0="+x1);
		
		if(xalpha>x1)
		{
			System.out.println("Uniformly Distributed");
		}
		else
		{
			System.out.println("Not Uniformly Distributed");
		}
 	}
}