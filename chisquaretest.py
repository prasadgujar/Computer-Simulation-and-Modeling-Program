# your code goes here
import random
#from scipy import stats
random_no=[]
N=100
for i in range(0,100):
	random_no.append((random.randint(1,99)*1.0)/100)
n=0
for e in range(5,101):
	if ((N*1.0)/e)%1==0:
		n=N/e
		break
n=10 #considering n as 10
newe=N/n
countarr=[]
marr=[]
for i in range(0,10,1):
	count=0
	for randno in random_no:
		if randno>=i/10 and randno<(i+1)/10:
			count=count+1
	countarr.append(count)
	marr.append(((count-newe)*(count-newe))/newe)
chi0=0
for m in marr:
	chi0=chi0+m

# uncomment this and scipy line if scipy library is installed
#chitable=stats.chi2.isf(0.050, n-1)  
chitable = 0.44
if chi0<chitable:
    for i in random_no:
        print(str(i)+", ", end =" ")
    print("\n Random numbers are uniformly distributed")
else:
    for i in random_no:
        print(str(i)+", ", end =" ")
    print("\n Random numbers are not uniformly distributed")
