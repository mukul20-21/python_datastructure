## utility function to check our given tym is sufficient or not..!!!
def validate(rank,n,ordered_para,limit):
	time = 0
	paratha = 0
	for i in range(n):
		time = rank[i]
		j = 2
		while (time<=limit):
			paratha +=1
			time = time+(rank[i]*j)
			j+=1
		if paratha>=ordered_para:
			return True
	return False
		
def main():
	t = int(input())
	while t:
		P = int(input())
		rank = list(map(int,input().split()))
		cook = rank.pop(0)
		
		low = 0
		high = max(rank)*(P*(P+1)//2)
		ans = 0
		while (low<=high):
			mid = (low+high)//2
			if validate(rank,cook,P,mid) == True:
				ans = mid
				high = mid-1
			else:
				low = mid+1
		print(ans)
		
		t-=1 
		
## Driver Code...!!!
if __name__ == "__main__":
	main()
	
'''
sample input..
3
10
4 1 2 3 4
8
1 1
8
8 1 1 1 1 1 1 1 1
'''