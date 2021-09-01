'''
Given a matrix mat[][] of size N x M, where every row and column is sorted in increasing order, and a number X is given.
The task is to find whether element X is present in the matrix or not.
'''
##method1 --> brute forces using linear traverse in matrix take time--> O(N)
##Method2 --> using binary search as given every row is in sorted order, search element in every list using binary search time --> O(NlogM)
'''
## According to given condition row-wise and column-wise matrix is sorted then we start from uppermost right side of matrix..

Example -->
            mat[row][col]
                :
        [[3 30 38]
        [44 52 54]
        [57 60 69]]
## Here row == 0
        col == len(matrix[0])-1

##Approach-->
        --if element is smaller than target element then shift col pointer towards left.
        --if element is greater than target element then shift row pointer towards down.

'''
def search(arr,N,M,X):
    row = 0
	col = M-1
	while (row<N and col>=0):
	    if (mat[row][col] == X):
	        return 1
        elif (mat[row][col]>X):
            col -=1
        else:
            row +=1
    return 0

'''
method4 --> using binary search if properties were mentioned..
This matrix has the following properties:

    --Integers in each row are sorted from left to right.
    --The first integer of each row is greater than the last integer of the previous row.

Appoarch --> 1. assign our virtual index on every element of matrix.
             2. now assign value for low and high element , low = 0 and high = total element in matrix.
             3. using above value find the value of mid but how to compare mid value its an 2-D array..
             4. to get row == mid//lenght of column , col = mid%lenght of column.
             5. Once we get the element then remaining process is same as binary search..
'''
def search_mat(matrix,target):

    N = len(matirx)
    M = len(matrix[0])
    ## bbase case...!!!
    if N == 0:
        return False
    low = 0
    high = (N*M) -1

    while low <= high:
        mid = low+(high-low)//2

        if (matrix[mid//M][mid%M] == target):
            return True
        elif (matrix[mid//M][mid%M] < target):
            low = mid+1
        else:
            high = mid-1

    return False

## Driver code..!!!!
if __name__ == "__main__":
    N,M,target = list(map(int,input().split()))
    mat = []
    for i in range(N):
        mat.append(list(map(int,input().split())))

    if search(mat,N,M,target):
        print('Element present in matrx')
    else:
        print('not found!!')
