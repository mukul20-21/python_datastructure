 ## first find intersection between two array and store its result and again take intersection b/w result and 3rd array..

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

## main function...!!!!
def commonElements (A, B, C, n1, n2, n3):

    res = intersection(A,n1,B,n2)              ## intersection element b/w arr1 and arr2
    final = intersection(C,n3,res,len(res))    ## intersection b/w previous result and arr3
    uni = []
    for i in final:
        if i not in uni:
            uni.append(i)

    return uni

## Driver code...!!!!!
if __name__ == "__main__":
    n1,n2,n3 = list(map(int,input().slit()))
    arr1 = list(map(int,input().slit()))
    arr2 = list(map(int,input().slit()))
    arr3 = list(map(int,input().slit()))
    print("common element-->",commonElements(arr1,arr2,arr2,n1,n2,n3))


'''
sample input
3 3 3
3 3 3
3 3 3
3 3 3
'''
