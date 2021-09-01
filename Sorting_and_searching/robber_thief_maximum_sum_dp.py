## use memoization to implement dynamic programming...!!!
def solve(i,arr,dp): ## parameter(index of array, input array, define dp table..)
	if i <= -1:
		return 0
	if dp[i] != -1:
		return dp[i]
    ## recursive calls
	op1 = arr[i] + solve(i-2,arr,dp)
	op2 = solve(i-1,arr,dp)
	## get maximum from both recursive calls...!!!!
	dp[i] = max(op1,op2)
	return dp[i]


## main function for calling and return value...!!!
def findmaxsum(arr,n):
	dp = [-1]*(n)
	## pass value from the last index of array..
	solve(n-1,arr,dp)
	return dp[n-1]
	

## Driver code...!!!
if __name__ == "__main__":
	n = int(input())
	arr = list(map(int,input().split()))
	print("maximum sum robber can get from houses-->",findmaxsum(arr,n))


"""
sample input...
6
5 5 10 100 10 5
"""
