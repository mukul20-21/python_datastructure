### binary search for infinite array element..!!!
def binary_search(arr,ele,start,end):
    mid = 0
    while start<=end:
        mid = (start+end)//2
        if(ele == arr[mid]):
            return arr[mid]
        elif(ele < arr[mid]):
            end = mid -1
        else:
            start = mid+1
           
    return -1
        
## code to get the correct value of start and end index from which we can bound the search element..!!!

def infinite_search(arr,ele):
    start = 0
    end = 1
    while(arr[end]<ele):
        start = end
        end = 2*end
    res = binary_search(arr,ele,start,end)
    return -1

## Driver code...!!!!
if __name__ == '__main__':
    ## infinite array which practical not possible to take input..
    ## it is a general code for it...
    arr = list(map(int,input().split()))
    ele = int(input())
    print('index of element in infinite sorted array..',infinite_search(arr,ele))