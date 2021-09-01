def binary_search(arr,ele):
    start = 0
    end = len(arr)-1
    mid = 0
    while start<=end:
        mid = (start+end)//2
        if (ele == arr[mid]):
            return mid
        ## left search
        elif(ele<arr[mid]):
            end = mid-1
        ## right search
        else:
            start = mid+1
    return -1

## driver code...!!!
if __name__ == '__main__':
    
    arr = list(map(int,input().split()))
    ele = int(input())
    print('index_of_given_element-->',binary_search(arr,ele))