# your code goes here
#import numpy as np

Dvalue = 0.565
a = [0.44,0.14,0.81,0.93,0.05]
a.sort()
b = [(i+1)/len(a) for i in range(len(a))]
dp = [b[i]-a[i] for i in range(len(a))]
dn = [a[i]-i/len(a) for i in range(len(a))]

maxd = max(max(dp),max(dn))
print (maxd)

if (maxd<Dvalue):
	print("Hypothesis accepted")
else:
	print("Hypothesis rejected")