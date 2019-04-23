# your code goes here# your code goes here
import math
#from scipy import stats

numlist=[0.89,0.17,0.99,0.46,0.05,0.66,0.10,0.42,0.18,0.49,0.37,0.51,0.54,0.01,0.81,0.28,0.69,0.34,0.75,0.49,0.72,0.43,0.56,0.97,0.30,0.94,0.96,0.58,0.73,0.05,0.06,0.39,0.84,0.24,0.40,0.64,0.40,0.19,0.79,0.68,0.18,0.26,0.97,0.88,0.64,0.47,0.60,0.11,0.29,0.78]
plusminus=[]
runs=[]
mean=0.495
n1=0
n2=0
for i in range(0,len(numlist)):
	if numlist[i]<mean:
		plusminus.append(1)
		n1=n1+1
	else:
		plusminus.append(0)
		n2=n2+1
flag=plusminus[0]

count=1
maxcount=1
for i in range(1,len(plusminus)):
	if plusminus[i]==flag:
		count=count+1
	elif plusminus[i]!=flag:
		if count>maxcount:
			maxcount=count
		runs.append(count)
		count=1
		flag=plusminus[i]
if count>maxcount:
	maxcount=count
	runs.append(count)

arunlens=[0,0,0,0,0]
for i in range(0,len(runs)):
	arunlens[runs[i]-1]=arunlens[runs[i]-1]+1

wi=[0,0,0,0,0]
for i in range(1,len(arunlens)+1):
	tempw=pow((n1/50),i)*(n2/50)+pow((n2/50),i)*(n1/50)
	wi[i-1]=tempw

ei=(n1/n2)+(n2/n1)
erunlens=[]
for i in range(len(arunlens)-1):
	erunlen=(50*wi[i])/ei
	erunlens.append(erunlen)
	
erunlast=50/ei
for i in range(0,len(erunlens)):
	erunlast=erunlast-erunlens[i]
	
erunlens.append(erunlast)
newerunlens=[]
newarunlens=[]
temprunlen=0
temparunlen=0
for i in range(len(erunlens)-1,-1,-1):
	if erunlens[i]<5:
		temprunlen=temprunlen+erunlens[i]
		temparunlen=temparunlen+arunlens[i]
		if(temprunlen>=5):
			newerunlens.append(temprunlen)
			temprunlen=0
			newarunlens.append(temparunlen)
			temparunlen=0
		else:
			newerunlens.append(erunlens[i])
			newarunlens.append(arunlens[i])
chi2=0
for i in range(0,len(newerunlens)):
	chi2=chi2+(((newarunlens[i]-newerunlens[i])*(newarunlens[i]-newerunlens[i]))/newerunlens[i])

#chitable=stats.chi2.isf(0.05, 2
 chitable = 0.525 //assume/find value froma table                       
	
if chi2<chitable:
	print("Hypothesis is not rejected")
else:
    print("rejected")
