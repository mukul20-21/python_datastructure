## function work with both +ive and -ive integer use dict = {sum,index} as a pair
def lenOfLongSubarr (arr, n, k) : 
	#Complete the function
	mydict = dict()
 	# Initialize sum and maxLen with 0
	summ = 0
	maxLen = 0
	# traverse the given array
	for i in range(n):
		summ += arr[i]
 	# when subArray starts from index '0'
		if (summ == k):
			maxLen = i + 1
	# check if 'sum-k' is present in mydict or not
		elif (summ - k) in mydict:
			maxLen = max(maxLen, i - mydict[summ - k])
	# if sum is not present in dictionary push it in the dictionary with its index
		if summ not in mydict:
			mydict[sum] = i
 
	return maxLen

## function with all positive integer use simple sliding window..
def lenOfLongSubarr (self, arr, n, k) : 
	maxx = -99999999
	i = 0
	j = 0
	summ = 0
	m = 0
	while j<N:
		summ += A[j]
		if summ < K:
			j+=1
		elif summ == K:
			m = max(m,j-i+1)
			j+=1
		else:
			while summ >K:
				summ -= A[i]
				i+=1
				if(summ==K):
					m = max(m,(j-i+1))
			j+=1
	return m	

## Diver Code...!!!!
if __name__ == "__main__":
	arr = list(map(int,input().split()))
	n,summ = list(map(int,input().split()))
	print(lenOfLongSubarr (arr, n, k))
'''
sample input..
1 4 3 3 5 5
6 16
'''