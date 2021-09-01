# find the first repeating element in an array integer..
t = int(input())
while t>0:
    matrix = []
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    dupl = set()
    for i in arr:
        if arr.count(i)>1:
            dupl.add(i)
     
    dupl = list(dupl)
    print(dupl[0])
    t = t-1