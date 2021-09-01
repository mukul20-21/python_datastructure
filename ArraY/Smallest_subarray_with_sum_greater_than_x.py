'''
Given an array of integers (A[])  and a number x, find the smallest subarray with sum greater than the given value.
Note: The answer always exists. It is guaranteed that x doesn't exceed the summation of a[i] (from 1 to N).
'''
def subarray_sum(arr, n, x):

    #Initialize current sum and minimum length
    curr_sum = 0
    min_len = n+1

    ##Initialize starting and ending indexes
    start = 0
    end = 0
    while (end < n):
        #Keep adding array elements while current sum is smaller than x
        while (curr_sum <= x and end < n):
            curr_sum += arr[end]
            end+=1

        ##If current sum becomes greater than x.
        while (curr_sum > x and start < n):
            ##Update minimum length if needed
            if (end - start < min_len):
                min_len = end - start

            curr_sum -= arr[start]
            start +=1

	if(min_len>n):
	    return 0
    return min_len

##Driver Code...!!!!
if __name__ == "__main__":
    N,X = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    print(subarray_sum(arr, n, x))

'''
A[] = {1, 4, 45, 6, 0, 19}
x  =  51
Output: 3
Explanation:
Minimum length subarray is
{4, 45, 6}
'''
