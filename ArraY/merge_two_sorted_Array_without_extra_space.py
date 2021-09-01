## method --> gap algorithm...
## function not return anything just update the value in same array in O(n+m) time...
## ceil function...
def nextGap(item):
    if (item <= 1):
        return 0
    return (item // 2) + (item % 2)

## main function not return any value..
def merge(arr1, arr2, n, m):
    summ = n+m
    gap = nextGap(summ)

    while gap>0:

        ## compare element in array1
        i = 0
        while i+gap<n:
            if arr1[i]>arr1[i+gap]:
                arr1[i],arr1[i+gap] = arr1[i+gap],arr1[i]   ## swap element..
            i+=1

        ## compare both arrays...
        # assign value for j..
        if gap > n:
            j = gap - n
        else:
            j = 0
        while i<n and j<m:
            if arr1[i] > arr2[j]:
                arr1[i],arr2[j] = arr2[j],arr1[i]
            i+=1
            j+=1

        ## COMPARE element in array2
        if (j<m):
            j = 0
            while j+gap < m:
                if arr2[j] > arr2[j+gap]:
                    arr2[j] ,arr2[j+gap] = arr2[j+gap],arr2[j]
                j +=1

    gap = nextGap(gap)

## Driver code...!!!!
if __name__ == "__main__":
    n,m = list(map(int,input().split()))
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))

    merge(arr1, arr2, n, m)
    print("merge and sort both array without space..")
    print(arr1)
    print(arr2)

'''
sample input...
4 5
1 3 5 7
0 2 6 8 9
'''
