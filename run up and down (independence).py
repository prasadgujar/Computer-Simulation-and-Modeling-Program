# your code goes here
import math

numlist=[0.52,0.99,0.46,0.58,0.64,0.25,0.88,0.11,0.20,0.18,0.97,0.44,0.43,0.94,0.82,0.60,0.73,0.69,0.21,0.03,0.04,0.81,0.85,0.30,0.47,0.96,0.17,0.72,0.62,0.27,0.10,0.60,0.34,0.65,0.79,0.44,0.02,0.37,0.48,0.50]

plusminus=[]
runs=[]
for i in range(0,len(numlist)-1):
	if numlist[i]<numlist[i+1]:
		plusminus.append(1)
	else:
		plusminus.append(0)
flag=plusminus[0]
count=1
for i in range(1,len(plusminus)):
	if plusminus[i]==flag:
		count=count+1
	elif plusminus[i]!=flag:
		runs.append(count)
		count=1
		flag=plusminus[i]
runs.append(count)

mean = (2*40-1)/3
variance = (16*40-29)/90

z0=(len(runs)-mean)/math.sqrt(variance)

if z0<=1.96 and z0>=-1.96:
	print("Hypothesis is not rejected")
else:
	print("Hypothesis rejected")
