'''
method1 --> linear traversal take time --> O(N*M)
method2 --> using binary search given in the question matrix is sorted row-wise. time -->O(N*logM)
            --here we first find the index of first 1's using binaray search and store the length and count of 1's using len_of_col - index.
            --Do this above step for each row and return the row index with maximum number of 1's count.
'''
'''
method3--> using property given in Question-- all row's is sorted. time --> O(N+M) (step-Ladder Problem).
            -- start from uppermost right corner element and check that element is 1 or not.
            -- traverse in starting row if 1 is present at last element if not jst update the row index.
            -- if 1 present at last index of row start decrease the col index pointer.
            -- store the index of max_row_index at every row.
'''
def rowWithMax1s(mat, n, m):
    row = 0
    col = m-1
    max_row_index=-1

    while row<n and col>=0 :
        if mat[row][col] == 1:
            max_row_index = row
            col-=1
        else :
            row+=1

    return max_row_index

## Driver code...!!!!!
if __name__ == "__main__":
    N,M = list(map(int,input().split()))
    mat = []
    for i in range(N):
        mat.append(list(map(int,input().split())))

    print('row with maximum 1's-->',rowWithMax1s(mat, n, m))

'''
sample input..
N = 4 , M = 4
Arr[][] = {{0, 1, 1, 1},
           {0, 0, 1, 1},
           {1, 1, 1, 1},
           {0, 0, 0, 0}}
Output: 2
Explanation: Row 2 contains 4 1's (0-based
indexing).
'''
