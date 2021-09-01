'''
Given a N x N matrix, where every row and column is sorted in non-decreasing order. Find the kth smallest element in the matrix.
'''
'''
Approach --> store element in list heapify it and return kth element using loop..
            -- same as array question kth_element in array.
'''
from heapq import heapify,heappop
def kthSmallest(mat, n, k):
    res = []
    for i in range(n):
        for j in range(n):
            res.append(mat[i][j])

    heapify(res)
    item = 0
    for i in range(k):
        item = heappop(res)
    return item

## Driver code..!!!!
if __name__ == "__main__":
    N = int(input())
    K = int(input())
    mat = []
    for i in range(N):
        mat.append(list(map(int,input().split())))
    print(kthSmallest(mat,N,K))
'''
sample input..!!!!
N = 4
mat[][] =   {{16, 28, 60, 64},
            {22, 41, 63, 91},
            {27, 50, 87, 93},
            {36, 78, 87, 94 }}
K = 3
Output: 27
Explanation: 27 is the 3rd smallest element.
'''
