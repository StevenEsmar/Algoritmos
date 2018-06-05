import itertools 
from random import randint
import sys

#Sort an Array and return number total of comparisons and swaps.
def BubbleSort(alist):
	stats=[]
	comparisons=0
	swaps=0
	for passnum in range(len(alist)-1,0,-1):
		for i in range(passnum):
			comparisons+=1
			if alist[i]>alist[i+1]:
				swaps+=1
				temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = temp

	stats.append(comparisons)
	stats.append(swaps)
	return stats #stats[0] = comparisons / stats[1] = swaps

#Return average comparisons and swaps from sorting all permutations of an Array
def GetAverageStats(Array):

	n=len(Array)
	perms =list(itertools.permutations(Array))
	np = len(perms)
	avgcomparisons=0
	avgswaps=0
	for i in range(np):
		lst= list(perms[i])
		stats=BubbleSort( lst)
		avgcomparisons += stats[0]
		avgswaps += stats[1]
	avgcomparisons /= float(np)
	avgswaps /= float(np)
	r=[]
	r.append(avgcomparisons)
	r.append(avgswaps)
	return r

#use given list of permutations
def ModGetAverageStats(Array):

	n=len(Array)
	avgcomparisons=0
	avgswaps=0
	for i in range(n):
		lst= list(Array[i])
		stats=BubbleSort( lst)
		avgcomparisons += stats[0]
		avgswaps += stats[1]
	avgcomparisons /= float(n)
	avgswaps /= float(n)
	r=[]
	r.append(avgcomparisons)
	r.append(avgswaps)
	return r


######MAIN#####

l= []
print "Insert n: (between 1 and  10)"
n=int(raw_input())
if (n>10 or n<1):
	print "invalid number!"
	sys.exit(0)

for i in range(n):
	l.append(i+1)
	k= GetAverageStats(l)
	print ("n="+str(i+1))
	print "Average Total instructions:"
	print (k[0]+k[1])
	print "Average comparisons:"
	print k[0]
	print "Average swaps:"
	print k[1]
	print "--------------------"
	if(i==n-1):
		perm = list(itertools.permutations(l))
		nperm = len(perm)
		randomperm=[]
		rlen = randint(1,nperm)
		print str(rlen) + " elements randomly picked."
		for j in range(rlen):
			randindex=randint(0,nperm-1)
			randomperm.append(list( perm[randindex] ) )
		k= ModGetAverageStats(randomperm)
		print ("Random sample of Permutations with  n="+str(i+1))
		print "Average Total instructions:"
		print (k[0]+k[1])																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																			
		print "Average comparisons:"
		print k[0]
		print "Average swaps:"
		print k[1]
		
