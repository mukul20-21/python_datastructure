def powercount(N,arr,bishu):
    count = 0
    solider = 0
    for i in range(N):
        if arr[i]<=bishu:
            count += arr[i]
            solider += 1
       
    print(solider,count)

def func(N,arr,Q,power):
    res = []
    for i in range(Q):
        res.append(powercount(N,arr,power[i]))
"""
method2 -- using prefix sum and binary search
def search(arr,element):
    start = 0
    end = len(arr)-1
    mid = 0
    while start<=end:
        mid = start +(end-start)//2
        if arr[mid] == element:
            return mid+1
        elif arr[mid]>element:
            end = mid-1
        else:
            start = mid+1
    
    return len(arr)

def func(N,arr,Q,power):
    arr.sort()
    prefix = [0]*(N+1)
    
    for i in range(1,N+1):
        prefix[i] = arr[i-1] + prefix[i-1]
    
    for i in range(Q):
        temp = search(arr,power[i])
        print(temp,prefix[temp])

"""
   

## Driver Code...!!!!
if __name__ == "__main__":
    N = int(input())
    arr = list(map(int,input().split()))
    Q = int(input())
    power = []
    for i in range(Q): 
        power.append(int(input()))
    
    func(N,arr,Q,power)

"""
sample input...
7
1 2 3 4 5 6 7
3
3
10
2
"""