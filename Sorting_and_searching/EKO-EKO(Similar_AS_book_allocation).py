# utility function...
def solve(arr,N,M,curr_blade):
	summ = 0
	for i in range(N):
		if (arr[i]>curr_blade):
			summ += arr[i]-curr_blade
	if (summ>=M):
		return True
	else:
		return False

## main calling function...
#height --> store the height of all trees to cutted..
# N --> total no. of trees..
# M --> minimum amount of wood is required by woodcutter..
def findbladeheight(height,N,M):
	height.sort()
	low = 0
	ans = 0
	high = height[-1]
	while (low<=high):
		mid = (low+high)//2
		if solve(height,N,M,mid)== True:
			ans = mid
			low = mid+1
		else:
			high = mid-1
	return ans


## DRiver code...!!!
if __name__ == "__main__":
	N,M = list(map(int,input().split()))
	height = list(map(int,input().split()))
	
	print("minimum height required to cut the tree-->",findbladeheight(height,N,M))
	
'''
sample input...
4 7
20 15 10 17
'''