from __future__ import print_function
def InsertionSort (Array):
	"Sort an array of integers using InsertionSort Algorithm"
	if (len(Array) == 1):
		return Array
	else:
		for i in range(1,len(Array)):
			x=i		
			while (x>0 and Array[x-1]>Array[x]):
				t=Array[x]
				Array[x]=Array[x-1]
				Array[x-1]=t
				x=x-1
				

	return Array
#-------------------End of Functions----------------

#-------------------Start of Main-------------------
if __name__ == '__main__':
	N=int(raw_input())
	a= [int(i) for i in raw_input().split()]
	s=list(a)
	s=InsertionSort(s)
	
	for i in range(N):
		f=a[i]
		idx = s.index(f)
		print (idx+1,end=" ")
	
