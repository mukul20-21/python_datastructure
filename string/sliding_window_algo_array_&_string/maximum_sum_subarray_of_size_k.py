def maxsumsubarray(arr,N,K):
	i = 0
	j = 0
	maxx = -9999999
	s = 0
	
	while j<N:
		s = s + arr[j]
		if (j-i+1)<K:
			j+=1
		elif (j-i+1) == K:
			maxx = max(s,maxx)
			s = s-arr[i]
			i +=1
			j +=1
	return maxx

## Driver code...!!!
if __name__ == "__main__":
	N,K = list(map(int,input().split()))
	arr = list(map(int,input().split()))
	print(maxsumsubarray(arr,N,K))
'''
sample input..
7 3
2 5 1 8 2 9 1
'''