## method --> separate out postive and negative in single interation and again swap alternative element to get desire o/p
def rearrange(arr):
    i = 0
    j = len(arr)-1
    n = len(arr)
    while i<=j:
        if arr[i]<0 and arr[j]>0:       ## if left is negative and right is positive swap both the element..
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j-=1

        elif arr[i]>0 and arr[j]<0:  ## if left is postive and right is negative jst update the pointer values..
            i+=1
            j-=1
        elif arr[i]>0:
            i+=1
        elif arr[j]<0:
            j-=1

    ## corner case if all element will negative or positive then jst return arr
    if (i==0 or i == n):
        return arr

    ## if above condition false then swap the element alternatively...
    else:
        k = 0       ## k store starting index and i --> store the first negative index of array after swap
        while k<n and i<n:
            arr[k],arr[i] = arr[i],arr[k]
            k+=2
            i+=1

        return arr

## Driver code...!!!!
if __name__ == "__main__":
    arr = list(map(int,input().split()))
    print(rearrange(arr))

'''
sample input...
1 2 3 -4 -1 4
'''
