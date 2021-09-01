def getPairsCount(arr, n, k):
    m = {}
    cnt = 0
    # loop to store freqeuncy of each element..
    for i in range(n):
        if arr[i] in m:
            m[arr[i]] = m[arr[i]]+1
        else:
            m[arr[i]] = 1

    for i in range(n):       ## check basic concept x = sum -arr[i] already present in array..
        x = k - arr[i]
        if x in m:
            cnt += m[x]     ## if x present update counter by its frequnecy..
        if x == arr[i]:
            cnt -= 1        ## if same element repeat twice consider only onces..

    return cnt//2

## Driver Code...
if __name__ == "__main__":
    n,k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    print("pair count",getPairsCount(arr,n,k))
