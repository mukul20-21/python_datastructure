n = int(input())
count = 0
while(n>0):
    n-=1
    k = list(map(int,input().strip().split()))
    if (sum(k)) >= 2:
        count+=1

print (count)
    
    