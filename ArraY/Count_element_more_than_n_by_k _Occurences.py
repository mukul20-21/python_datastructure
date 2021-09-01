'''
Given an array arr[] of size N and an element k. The task is to find all elements in array that appear more than n/k
'''
## just store the freqency in array into a dictionary with (element,frequency) as pair..
## once add all element and then cnt the n//k values from the dictionary values..
def countOccurence(arr,n,k):
    m = {}
    for i in arr:
        m[i] = m.get(i,0) + 1

    cnt = 0
    for i in m:
        if m[i] > n//k:
            cnt+=1

    return cnt

## Driver code...!!!!
if __name__ == "__main__":
    n,k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    print('count of n//k element in array',countOccurence(arr,n,k))

'''
sample input
N = 8 k = 4
arr[] = {3,1,2,2,1,2,3,3}
Output: 2
Explanation: In the given array, 3 and 2 are the only elements that appears more than n/k times.
'''
