## hashmap and prefix sum..
def findsubarray(arr,n):
	hashMap = {}
	res = 0
    
	sum1 = 0
	for i in range(n):
		sum1 += arr[i]
         
	# if sum is 0, we found a subarray starting from index 0 and ending at index i
		if sum1 == 0:
			res +=1
		al = []
	 # If sum already exists in the map there exists at-least one subarray ending at index i with 0 sum
		if sum1 in hashMap:
             # map[sum] stores starting index of all subarrays
			al = hashMap.get(sum1)
			for j in range(len(al)):
				res +=1
		al.append(i)
		hashMap[sum1] = al
        
	return res

### Driver code...!!!
if __name__ == "__main__":
	n = int(input())
	arr = list(map(int,input().split()))
	print("total no of subarray with (sum == Zero) is-->",findsubarray(arr,n))
	
'''
sample input...
6
0 0 5 5 0 0
'''