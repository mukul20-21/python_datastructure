## using pattern observe method...
## using 4 steps we get the next permutation..

## utility function to reverse array..
def reverse(arr,start,end):
    while start<end:
        arr[start],arr[end] = arr[end],arr[start]
        start+=1
        end -=1


## main function...!!!!

def next_permutation(arr):
    n = len(arr)
    k = 0  ## store index1
    l = 0  ## store index2

    #step1 --> find break point..
    for k in range(n-2,-1,-1):
        if (arr[k] <= arr[k+1]):
            break
    ## exception point if no break point obtain and k == -1
    #if k< 0:
    #    reverse(arr,0,len(arr)-1)

    ## step2 --> get replacing item jst greater than idx1 element.. iterate b/w l to k value..
    if k>=0:
        for l in range(n-1,l>k,-1):
            if arr[l]>arr[k]:
                break

        ## step3 --> swap the element..
        arr[k],arr[l] = arr[l],arr[k]
    ## step4 --> get minimum possible value..
    reverse(arr,k+1,len(arr)-1)

    return arr

## Above function not work with for loop correctly here is same function implementation using while loop...
def next_pre(arr):
    i = len(arr)-2
    while (i >= 0 and arr[i+1] <= arr[i]):    ## step1 --> get the breaking point..
        i-=1

    if (i >= 0):
        j = len(arr) - 1
        while (arr[j] <= arr[i]):   ## step2 --> getting most nearest replacing element index,,,
            j-=1
        #step3--> swap the element
        arr[i],arr[j] = arr[j],arr[i]

    # step4 --> get minimum possible value..
    reverse(arr,i+1,len(arr)-1)
    return arr


## Driver code...!!!!!
if __name__ == "__main__":
    arr = list(map(int,input().split()))
    print(next_permutation(arr))

'''
sample input...
1 3 5 4 2
'''
