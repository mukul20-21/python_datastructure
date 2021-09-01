## minimum diffrence element in a sorted array...!!!
## given a sorted array and key find the element in array how diffrence is minimum..
'''
ex:::input--> arr:[4,6,10] and key = 7
    :output --> 6 because (7-6 = 1)
    first approach --> problem is as similar with the finding the floor and ceil value..!!!
    second approach --> apply binary search if element not found return the min between the abs diffence of elment,start & end..
    
'''


def binary_search(arr,ele):
    start = 0
    mid = 0
    end = len(arr)-1
    res = -1
    while start<=end:
        mid = (start+end)//2
        if(ele == arr[mid]):
            return arr[mid]
        # if element is smaller..
        elif(ele < arr[mid]):
            end = mid-1
        else:
            start = mid+1
    
    res1 = abs(ele-arr[start])
    res2 = abs(ele-arr[end])
    if res1<res2:
        return arr[start]
    else:
        return arr[end]
        

## Driver code...!!!!!
if __name__ == '__main__':
    arr = list(map(int,input().split()))
    ele = int(input())
    print('minimum diffrence of given element is-->>>',binary_search(arr,ele))