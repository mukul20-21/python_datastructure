def check(num,stalls,C):
	cows=1
	pos=stalls[0]
	for i in range(len(stalls)):
		if (stalls[i]-pos>=num):
			pos=stalls[i]
			cows += 1
			if (cows==C):
				return 1
	return 0


def binarySearch(stalls,C):
	stalls.sort()
	start=0
	end=stalls[-1]
	maxx= -1
	while (end>start):
		mid=(start+end)//2
		if (check(mid,stalls,C)==1):
			if (mid>maxx):
				maxx=mid
			start=mid+1
		else:
			end=mid
	
	print(maxx)


## DRIVER CODE...!!!
if __name__ == "__main__":
	
	t = int(input())
	while (t):
		N,C = list(map(int,input().split()))
		stalls = []
		for i in range(N):
			stalls.append(int(input()))
		print("minimum largest distance")	
		binarySearch(stalls,C)
			
		t-=1

'''
sample input..
1
5 3
1
2
8
4
9
'''
