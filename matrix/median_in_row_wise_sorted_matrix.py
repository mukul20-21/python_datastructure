'''
method1--> Using Brute Force --> time - O(N^MlogN^M); space - O(N*M)
        --store element into list using two loop.
        --Sort the array.
        --Return the median of that sorted list.

'''
def median_matrix(mat,N,M):
    res = []
    for i in range(N):
        for j in range(M):
            res.append(mat[i][j])
    res.sort()
    n = len(res)
    return res[n//2]

'''
method2 --> Using Nested Binary Search..
Approach::
            -- use outer binary search to get middle element from given range of element in matrix.
            -- Now count no. of element lesser than equal to middle element using binary search.
            -- Again use inner/nested binary search to find no.of element lesser than equal to given middle element.

            -- Using count of element from inner binary search we shrink the range in inner binary search.
            -- In inner binary search we compare element which pass from outer binary search..
'''
## utility function.... TO find count of element less than equal to given outer binary search middle element..
def countsmallerthanmid(row:list,mid):
    l = 0
    h = len(row) - 1
    while(l <= h):
        md = (l + h) >> 1
        if(row[md] <= mid):
            l = md + 1
        else:
            h = md - 1;

    return l

## Main function to find the median...
def findmedian(matrix,R,C):
    low = 1
    high = 2000  ## as given in contraint of question..

    while (low<=high):
        mid = (low + high)>>1
        cnt = 0
        for i in range(R):
            cnt += countsmallerthanmid(matrix[i],mid)

        if cnt<= (R+C)//2:
            low = mid+1
        else:
            high = mid-1

    return low

## Driver code...!!!!
if __name__ == "__main__":
    N,M = list(map(int,input().split()))
    mat = []
    for i in range(N):
        mat.append(list(map(int,input().split())))

    print('median of given matrix',findmedian(mat,N,M))

'''
R = 3, C = 3
M = [[1, 3, 5],
     [2, 6, 9],
     [3, 6, 9]]

Output: 5
'''
