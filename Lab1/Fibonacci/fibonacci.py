import matplotlib.pyplot as plt 
import numpy as np 
import sys
import time
#Create variables and assign their initial values.



IntFn_2=0
IntFn_1=1
IntFn=0
n= 100
overFlow=0
x=[]
for i in range(n):
    startTime=time.time()
    IntAux=IntFn 
    IntFn_2=IntFn_1
    IntFn_1=IntFn
    IntFn=IntFn_2+IntFn_1
    duration=(time.time()-startTime)
    x.append(int(duration*1000000000))
    #--------------------
    if(IntFn>sys.maxint and overFlow==0):
        print ("Overflow computing "+str(i+1)+"-th term of Fibonacci Sequence(data type: Int) ");
        print(str(i)+"-th term is: "+str(IntFn_1)+" and the next one is: "+str(IntFn))
        overFlow=1
        print ("Max int: "+str(sys.maxint))        
plt.plot(x);
plt.xlabel('n');
plt.ylabel('time (nanoseconds)');
print "--------------------------"
print(np.mean(x))
print(np.std(x))
