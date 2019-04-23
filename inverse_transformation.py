#import numpy as np
import math

# LCM to generate initial random no.'s

N = int(input("Enter total number random variables required : "))
# seed value
x0 = int(input("Enter seed value : "))
a = 171525251
m = 101
c = 454687987
l = []
l.append(x0)

for i in range(1,N):
    l.append(((a*l[i-1] + c) % m)) 

l = [round(x/m, 2) for x in l]
print('Random Numbers: {}'.format(l))

def exp_d():
    lamb = float(input("Enter mean life time : "))
    new_l = [-math.log(i)/lamb for i in l]
    print("Corresponding Random Variates : {}".format(new_l))

def uniform_d():
    a = float(input("Enter max value (a) : "))
    b = float(input("Enter min value (b) : "))
    new_l = [i*(b-a) + a for i in l]
    print("Corresponding Random Variates : {}".format(new_l))

def weibull_d():
    alpha = float(input("Enter scale parameter : "))
    beta = float(input("Enter shape parameter : "))
    new_l = [ alpha *  math.pow(-math.log(1-i) , 1/beta) for i in l]
    print("Corresponding Random Variates : {}".format(new_l))

def triangular_d():
    a = float(input("Enter max value(a) : "))
    b = float(input("Enter most likely value(b) : "))
    c = float(input("Enter min value(c) : "))
    new_l = []
    for i in range(len(l)):
        if(l[i] > 0 and (b-a)/(c-a) >= l[i]):
            new_l.append(math.pow(l[i]*(b-a)*(c-a), 0.5) + a)
        else:
            new_l.append(math.pow((1-l[i])*(c-b)*(c-a), 0.5))
            
    # new_l = [ alpha *  math.pow(-math.pow(1-i), 1/beta) for i in l]
    print("Corresponding Random Variates : {}".format(new_l))

ch = 0
while ch != 5:
    print("\n#############Choose Distribution##################")
    print("\n1. Exponential\n2. Uniform\n3. Weibull\n4. Triangular\n5. Exit")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        exp_d()
    elif ch == 2:
        uniform_d()
    elif ch == 3:
        weibull_d()
    elif ch == 4:
        triangular_d()
    else :
        exit()    
