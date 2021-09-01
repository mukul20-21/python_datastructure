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
    
   

## Driver Code...!!!!
if __name__ == "__main__":
    N = int(input())
    arr = list(map(int,input().split()))
    Q = int(input())
    power = []
    for i in range(Q):
        temp = int(input())
        power.append(temp)
    
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