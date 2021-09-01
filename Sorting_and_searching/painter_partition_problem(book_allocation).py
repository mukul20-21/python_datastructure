## utility function to validate our given mid valued used or not...
def check(arr,n,limit):
    summ = 0
    painters = 1
    
    for i in range(n):
        summ += arr[i]
        if (summ>limit):
            summ = arr[i]    ## if limit exceed jst reassign value..
            painters += 1
    return painters


def minTime (arr, n, k):
	low = max(arr)   ## assign maximum as a lower bound..
	high = sum(arr) ## assign upper bound as sum of length of total boards
	
	while(low<high):
		mid = (low+high)//2
		painters = check(arr,n,mid)
		if painters <= k:
			high = mid
		else:
			low = mid+1

	return low

	
## Driver code...!!!!
if __name__ == "__main__":
	N,painter = list(map(int,input().split()))
	board = list(map(int,input().split()))
	print("minimum time for completing the job..",minTime(board,N,painter))

'''
sample input...
5 3
5 10 30 20 15
'''