'''
Given an NxN matrix Mat. Sort all elements of the matrix.
'''
'''
sample input...
Input:
N=4
Mat=[[10,20,30,40],
[15,25,35,45]
[27,29,37,48]
[32,33,39,50]]
Output:
10 15 20 25
27 29 30 32
33 35 37 39
40 45 48 50
Explanation:
'''
## Method1--> using sorting + traversal of matrix twice.. time--> O(N^2)
def sortedMatrix(Mat,N):
    res = []
    for i in range(N):
        for j in range(N):
            res.append(Mat[i][j])

    res.sort()
    k = 0
    for i in range(N):
        for j in range(N):
            Mat[i][j] = res[k]
            k+=1

    return Mat

## Driver code...!!!!
if __name__ == "__main__":
    N = int(input())
    mat = []
    for i in range(N):
        mat.append(list(map(int,input().split())))
    print(sortedMatrix(mat,N))
