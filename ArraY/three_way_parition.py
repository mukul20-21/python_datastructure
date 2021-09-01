'''
Given an array of size n and a range [a, b]. The task is to partition the array around the range such that array is divided into three parts.
1) All elements smaller than a come first.
2) All elements in range a to b come next.
3) All elements greater than b appear in the end.
The individual elements of three sets can appear in any order. You are required to return the modified array.
'''
## Using two pointer approach...
def threeWayPartition(array, a, b):
    n = len(array)
	#Using two pointers which help in finding the index with which the elements need to be swapped if they are not in correct position.
	s = i = 0
	e = n-1

	while(i <= e):
        #If current element is smaller than lower range, we swap it with value on next available smallest position.
		if array[i] < a:
			array[i],array[s] = array[s],array[i]
			i+=1
			s+=1
		#If current element is greater than higher range, we swap it with value on next available greatest position.
		elif array[i] > b:
			array[i],array[e] = array[e],array[i]
			e-=1
		#Else we just move ahead in the array.
		else:
			i+=1

## Driver code...!!!!
if __name__ == "__main__":
    a,b = list(map(int,input().split()))
    arr = list(map(int,input().split()))

'''
sample input..
n = 5
A[] = {1, 2, 3, 3, 4}
[a, b] = [1, 2]
Output: 1
Explanation: One possible arrangement is:{1, 2, 3, 3, 4}. If you return a valid arrangement, output will be 1.
'''
