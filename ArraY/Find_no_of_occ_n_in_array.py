# Given an number n. Find the number of occurrences of n in the array.

def count(arr,n,m):
	count = 0
	for i in range(m):
    	if arr[i] == n:
        	count = count+1
    	else:
        	continue
	return count
## Driver code...!!!!
if __name__ == "__main__":
	n,m = map(int,input("Element occurs: & size of array").strip().split())
	arr = list(map(int,input("Enter the element in array").strip().split()))[:m]
	print("Enter element repeats:",count(arr,n,m),"Times..!!" )
