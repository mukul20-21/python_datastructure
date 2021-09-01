## find the key in rowwise and column wise sorted matrix..!!!!
## Initialize our asume mid element to topmost right corner..

def search_matrix(mat,key,n,m):
    i = 0
    j = m-1
    while(i>=0 and i<n and j>= 0 and j<m):
        if (arr[i][j] == key):
            return i,j
        elif(arr[i][j]>key):
            j-=1
        elif(arr[i][j]<key):
            i+=1
    return -1
    
## Driver code..!!!
if __name__ == '__main__':
    n,m = list(map(int,input().split()))
    key = int(input())
    mat = [[list(map(int,input().split()))]for i in range(n)]
    print('index of key',search_matrix(mat,key,n,m))
    
    
        