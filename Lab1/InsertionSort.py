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

if __name__ == '__main__':
	N=int(raw_input())
	vampires=[] #odd
	totV=0
	zombies=[] #even
	totZ=0
	for i in raw_input().split():
		if (int(i)%2==0):
			zombies.append(int(i))
			totZ=totZ+int(i)
		else:
			vampires.append(int(i))
			totV=totV+int(i)
	InsertionSort(zombies)
	InsertionSort(vampires)
	zombies.append(totZ)
	vampires.append(totV)
	for i in zombies:
		print(i, end=" ") 
	for i in vampires:
		print(i, end= " ") 
