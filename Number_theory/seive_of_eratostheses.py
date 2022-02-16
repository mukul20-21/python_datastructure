## Spoj problem solution..!!!!
## Genrate prime number upto 90 million and print accordingly...!!!

def seive(ans):
    maxN = 90000000
    prime = [True for i in range(maxN + 1)]
    prime[0] = False
    prime[1] = False

    i = 2
    while(i*i <= maxN):
        if prime[i]== True:
            for j in range(i**2,maxN+1,i):
                prime[j] = False
        i+=1

    for i in range(maxN+1):
       if prime[i]:
           ans.append(i)
    return ans

## Driver code...!!!!
if __name__ == "__main__":

    ans = [] ## list to store prime number for given range..!!!!
    t = int(input())
    res = [] ## Temp list to store elements from user input..!!!
    for i in range(t):
        res.append(int(input()))

    seive(ans)
    for i in res:
        print(ans[i-1])
