## method1 --> create all possible subarray and return maximum subarray..!!!
def subarraysum(arr):
    n = len(arr)
    res = -9999999
    temp = 0
    for i in range(n):
        for j in range(i,n):
            temp +=arr[j]
        res = max(temp,res)
        temp = 0
    return res

## Method2 --> kadane's algorithm to find maximum sum of continous subarray..!!!
def kadane_Algo(arr):
    sum = 0
    maxi = -99999999
    for i in range(len(arr)):
        sum += arr[i]
        maxi = max(maxi,sum)
        if sum<0:
            sum = 0
    return maxi

## Driver code...!!!
if __name__ == "__main__":
    arr = list(map(int,input().split()))
    print("maximum continous subarray sum-->",kadane_Algo(arr))

'''
sample input...
1 2 3 -2 5
'''
