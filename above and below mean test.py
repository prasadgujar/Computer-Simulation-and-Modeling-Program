# your code goes here
import math
r=[0.41,0.68,0.89,0.94,0.74,0.91,0.55,0.62,0.36,0.27,0.19,0.72,0.75,0.08,0.54,0.02,0.01,0.36,0.16,0.28,0.18,0.01,0.95,0.69,0.18,0.47,0.23,0.32,0.82,0.53,0.31,0.42,0.73,0.04,0.83,0.45,0.13,0.57,0.63,0.29]
N = len(r)
seq = ""

n1 = 0
n2 = 0
for i in range(0,len(r)):
	if(r[i]>0.495):
		seq = seq+"+"
		n1 = n1+1
	else:
		seq = seq + "-"
		n2 = n2+1
count = 1
char = seq[0]
for i in range(1,len(seq)):
	if(seq[i]!=char):
		count = count+1
		char = seq[i]
		
# mean and variance

mu = (2*n1*n2/N)+0.5
temp = 2*n1*n2

var = (temp**2-temp*N)/(N**3-N**2)
z0 =(count-mu)/math.sqrt(var)
if(z0>=-1.96 and z0<=1.96):
	print("Numbers are independent based on runs above and below mean")
else:
	print("Numbers are independent")