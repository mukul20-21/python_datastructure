#Function to find maximum of each subarray of size k.
def max_of_subarrays(arr,n,k):
	l = []
	ans = []
	i = 0
	j = 0
        
	while j<n:
		while (len(l)>0 and l[-1] < arr[j]): ## check previous element in l list < arr[j] then jst remove and stop when list is empty..
			l.pop()
		l.append(arr[j])
            	
		if j-i+1 <k:
			j+=1
		elif j-i+1 == k:
			ans.append(l[0])
			if (l[0] == arr[i]):        ## check after append into result appended element is important or not..!!!
				l.pop(0)
			i+=1
			j+=1
	return ans

##Driver code...!!!!!
if __name__ == "__main__":
	n,k = list(map(int,input().split()))
	arr = list(map(int,input().split()))
	
	print("maximum from all subarray of size k-->",max_of_subarrays(arr,n,k))

'''
sample input..
9 3
1 2 3 1 4 5 2 3 6
'''
