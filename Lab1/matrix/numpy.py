import time
import numpy as np
print "Enter an n:"
n= 30 #put your n
A=np.array([[],[]], np.int32)
B=np.array([[],[]], np.int32)
C=np.array([[],[]], np.int32)
mean =0

r=n
c=n
A=[1]*r
B=[1]*r
C=[1]*r
for i in range(r):
    A[i]=[1]*c
    B[i]=[2]*c
    C[i]=[1]*c

for row in range(n):
    for col in range(n):
        result=0
        for m in range(n):
            startTime = time.time()
            result= result + A[row][m]*B[m][col]  
            duration = (time.time() - startTime)
            mean= mean + duration
            print (int(duration*1000000000))

        C[row][col] = result
        #System.out.print(result + " ");
        #System.out.print("\n");

print "---------"
print (mean/(n*n*n))
