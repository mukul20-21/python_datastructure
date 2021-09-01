## single function handle every thing...
def main():
    t = int(input())
    while t:
        n,q = list(map(int,input().split()))
        v = []
        for i in range(n):
            v.append(list(map(int,input().split())))
    
        v.sort()
        idx = 0
        first = 0
        second = 1
        for i in range(1,len(v)):
            if v[idx][second] >= v[i][first]:
                v[idx][second] = max(v[idx][second] ,v[i][second])
            else:
                idx +=1
                v[idx] = v[i]
        
        while q:
            k = int(input())
            ans = -1
            for i in range(idx+1):
                if (v[i][second] - v[i][first] +1) > k:
                    ans = v[i][first]+k-1
                    break
                else:
                    k = k - (v[i][second] - v[i][first] +1)
            print(ans)
            q-=1
        t-=1

        
## Driver code....
if __name__ == "__main__":
    main()

"""
sample input..
1
1 3
1 5
1
3
6
"""