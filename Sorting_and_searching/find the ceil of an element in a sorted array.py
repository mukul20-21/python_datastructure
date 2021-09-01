## binary search to find the ceil element of sorted array...!!!

def binary_search(arr,ele):
    start = 0
    mid = 0
    end = len(arr)-1
    res = -1
    while start<=end:
        mid = (start+end)//2
        if(ele == arr[mid]):
            return arr[mid]
        ## move left if ele is greater than mid..!!!
        elif(ele > arr[mid]):
            start = mid+1
        ## move right if mid is smaller than mid..!!!
        elif(ele < arr[mid]):
            res = arr[mid]
            end = mid-1
           
    return res
        

## Driver code...!!!!!
if __name__ == '__main__':
    arr = list(map(int,input().split()))
    ele = int(input())
    print('ceil of given element is-->>>',binary_search(arr,ele))