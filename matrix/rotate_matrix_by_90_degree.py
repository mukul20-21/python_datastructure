## Effcient approach -->  Tranpose + reverse matrix...
'''
Approach -->
        -- First get the transpose of given matrix (replace 1st column with 1st row).
        -- After doing transpose for each row jst reverse the every row one by one..

        -- Step1 -- Transpose
        --Step2 -- Reverse every row..
'''
def rotate(matrix):
    N = len(matrix)

    ## Step--1 transpose of matrix...
    for i in range(N):
        for j in range(i):
            matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]   ## Swap element of column with row..

    ## Step2 -- reverse matrix columnwise..
    for i in range(N):
        matrix[i] = matrix[i][::-1]

    return matrix

## Driver code...!!!!
if __name__ == "__main__":
    N = int(input())
    mat = []
    for i in range(N):
        mat.append(list(map(int,input().split())))

    print("Before rotation matrix",mat)
    print()
    print('rotated matrix by 90 degree-->',rotate(mat))

'''
sample input...
3
1 2 3
4 5 6
7 8 9

o/p-->
7 4 1
8 5 2
9 6 3
'''
