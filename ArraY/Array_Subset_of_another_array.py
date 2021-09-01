## Simple method --> use hashmap store all element of array1 and check array2 all element present or not...
'''
Given two arrays: a1[0..n-1] of size n and a2[0..m-1] of size m. Task is to check whether a2[] is a subset of a1[] or not.
Both the arrays can be sorted or unsorted. It may be assumed that elements in both array are distinct.
'''
def isSubset( a1, a2, n, m):
    m = {}
    for i in a1:
        m[i] = m.get(i,0)+1

    for i in a2:
        if i not in m:
            return 'No'
    return 'Yes'

## Driver code...!!!!
if __name__ == "__main__":
    N,M = list(map(int,input().split()))
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    print('given array2 is subset of array1-->',isSubset(arr1,N,arr2,M))

'''
sample input...
Input:
a1[] = {11, 1, 13, 21, 3, 7}
a2[] = {11, 3, 7, 1}
Output:
Yes
Explanation:
a2[] is a subset of a1[]
'''
