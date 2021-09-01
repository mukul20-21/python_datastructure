## Using two pointer approach to get union and intersection...
def union(arr1,N,arr2,M):
    res = []
    i = 0
    j = 0
    while i<N and j<M:
        if arr1[i]<arr2[j]:         ##If arr1[i] is smaller than arr2[j] then print arr1[i] and increment i.
            res.append(arr1[i])
            i +=1
        elif arr1[i]>arr2[j]:         ##If arr1[i] is greater than arr2[j] then print arr2[j] and increment j.
            res.append(arr2[j])
            j +=1
        elif arr1[i]== arr2[j]:     ##If both are same then print any of them and increment both i and j.
            res.append(arr1[i])
            i+=1
            j+=1
    #Print remaining elements of the larger array..
    while i<N:              ## if element remaining in array1..
        res.append(arr1[i])
        i+=1
    while j<M:              ## if element remaining in array2..
        res.append(arr2[j])
        j+=1
    return res

def intersection(arr1,N,arr2,M):   ## print common element in both array..
    res = []
    i = 0
    j = 0
    while i < N and j < M:
        if arr1[i] < arr2[j]:               ## if arr1[i] smaller than arr2[j] increment i++
            i += 1
        elif arr2[j] < arr1[i]:             ## if arr1[i] greater than arr2[j] increment j++
            j+= 1
        else:                               ## if both same increment both pointer and append(any one..)
            res.append(arr2[j])
            j += 1
            i += 1
    return res

## Driver Code...!!!!
if __name__ == "__main__":
    N,M = list(map(int,input().split()))
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    print("union-->",union(arr1,N,arr2,M))
    print("Intersection-->",intersection(arr1,N,arr2,M))

'''
sample input...!!!!
5 3
1 2 3 4 5
1 2 3
'''
