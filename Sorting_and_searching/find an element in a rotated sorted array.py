def binary_search(arr,ele,start,end):
    
    mid = 0
    while start<=end:
        mid = (start+end)//2
        if (ele == arr[mid]):
            return mid
        elif(ele < arr[mid]):
            end = mid-1
        else:
            start = mid+1
    return -1
    
## no of times array rotate = index of minimum element..!!!!
def binary_element(arr,ele):
    start = 0
    end = len(arr)-1
    mid = 0
    N=len(arr)
    #index = -1
    while start<=end:
        mid = (start+end)//2
        if (arr[mid]< arr[((mid+N-1)%N)] and arr[mid]<arr[((mid+1)%N)]):
            return mid
            #return index
            
        elif(arr[mid] > arr[mid+1]):
            start = mid+1
        else:
            end = mid-1
    return -1
    

## driver code...!!!
if __name__ == '__main__':
    
    arr = list(map(int,input().split()))
    ele = int(input())
    N = len(arr)
    index = binary_element(arr,ele)
    print(index)
    ## left and right binary search..!!!
    left = binary_search(arr,ele,0,index-1)
    right = binary_search(arr,ele,index+1,N-1)
    if left > -1:
        print(left)
    else:
        print(right)