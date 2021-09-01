def binary_search(arr,ele):
    ## first occurance...!!!!
    start = 0
    end = len(arr)-1
    mid = 0
    count = 0
    first = -1
    while start<=end:
        mid = (start+end)//2
        if (ele == arr[mid]):
            first = mid
            count+=1
            end = mid-1
        elif(ele<arr[mid]):
            end = mid-1
        else:
            start = mid+1
    ## last occurance
    start = 0
    mid = 0
    end = len(arr)-1
    last = -1
    while start<=end:
        mid = (start+end)//2
        if (ele == arr[mid]):
            last = mid
            start = mid+1
            count+=1
        elif(ele<arr[mid]):
            end = mid-1
        else:
            start = mid+1
    
    return count

## driver code...!!!
if __name__ == '__main__':
    
    arr = list(map(int,input().split()))
    ele = int(input())
    print(f'count_of_{ele} is-->',binary_search(arr,ele))