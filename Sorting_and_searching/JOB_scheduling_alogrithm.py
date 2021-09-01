def jobScheduling(startTime, endTime, profit):
	n = len(startTime)
	v = []
	for i in range(n):
		v.append([startTime[i],endTime[i],profit[i]])
	
	v.sort(key = lambda x: x[1])
	# 0--> starting time , 1--> finishing time , 2 --> profit on job..
	dp = [-1]*(n)
	dp[0] = v[0][2]
        	
	for i in range(1,n):
		inc = v[i][2]
		last = -1
		low = 0
		high = i-1
            
		while low<=high:
			mid = (low + high)//2
			if (v[mid][1]<=v[i][0]):
				last = mid
				low = mid+1
			else:
				high = mid-1
                
		if last!= -1:
			inc += dp[last]
		exc = dp[i-1]
		dp[i] = max(inc,exc)
        
	return dp[n-1]

## Driver code...!!!!
if __name__ == "__main__":
	start = list(map(int,input().split()))
	finish = list(map(int,input().split()))
	profit = list(map(int,input().split()))
	
	print("maximum profit-->",jobScheduling(start,finish,profit))

'''
sample input..
1 2 3 3
3 4 5 6
50 10 40 70
o/p --> 120
'''