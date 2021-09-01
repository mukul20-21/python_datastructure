## binary search to find the next aplhabetic element...!!!

def binary_search(arr,ele):
    start = 0
    mid = 0
    end = len(arr)-1
    res = -1
    while start<=end:
        mid = (start+end)//2
        ## move left if element is smaller..!!!
        if (ele < arr[mid]):
            res = mid
            end = mid -1
        else:
            start = mid+1
        
    if (arr[res]< ele):
        return arr[0]
    else:
        return arr[res]
           
    #return res
        

## Driver code...!!!!!
if __name__ == '__main__':
    arr = list(input())
    ele = input()
    print('next alphabet is-->>>',binary_search(arr,ele))