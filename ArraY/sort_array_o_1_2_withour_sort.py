""" Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algorithm."""
def sort012(arr,n):
    low=0
    high=n-1
    mid=0
    while mid<=high:
        if arr[mid]==0:
            arr[mid] , arr[low] = arr[low] , arr[mid]
            mid+=1
            low+=1

        elif arr[mid]==1:
            mid+=1

        else:
            arr[mid] , arr[high] = arr[high] , arr[mid]
            high-=1
    return arr

## Driver code..!!!!!
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split()))
'''
sample input...
5
0 2 1 2 0
'''
