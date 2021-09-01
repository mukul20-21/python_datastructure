## binary search algorithm with updation..
## time-->O(log(min(n,m))) ,,, space --> O(1)

def kthElement(arr1, arr2, k):
	n = len(arr1)
	m = len(arr2)
	if(n > m): 
		return kthElement(arr2, arr1, k); 
        
	low = max(0,k-m) 
	high = min(k,n)
	INT_MIN = -99999999
	INT_MAX = 99999999
	while(low <= high):
		cut1 = (low + high)//2 
		cut2 = k - cut1 
        ## Edges cases...!!!    
		
		
		l1 = INT_MIN if cut1 == 0 else arr1[cut1 - 1]   ## when split with first element of array
		l2 = INT_MIN if cut2 == 0 else arr2[cut2 - 1]
		
		r1 = INT_MAX if cut1 == n else arr1[cut1]   ## when split happens to last element of array...
		r2 = INT_MAX if cut2 == m else arr2[cut2]
			
		## check given validing condition... 
		if(l1 <= r2 and l2 <= r1): 
			return max(l1, l2)
		elif (l1 > r2): 
			high = cut1 - 1
		else:
			low = cut1 + 1

## Driver code...!!!!
if __name__ == "__main__":
	arr1 = list(map(int,input().split()))
	arr2 = list(map(int,input().split()))
	k = int(input())
	print("kth element in both sorted array is--->", kthElement(arr1, arr2, k))
	
"""
sample input...
2 3 6 7 9
1 4 8 10
5
"""