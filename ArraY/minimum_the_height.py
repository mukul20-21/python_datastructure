## method --> use sliding window technique with some modification..
def getmindiff(arr,n,k):
    pair = []
    vis = [0]*(n)

    for i in range(n):
        if (arr[i]-k>=0):
            pair.append([arr[i]-k,i])       ## store pair [height,index]
        pair.append([arr[i]+k,i])

    pair.sort()
    ele = 0
    left = 0
    right = 0

    ## first loop to get window size == n:
    while(ele < n and right < len(pair)):
        if (vis[pair[right][1]] == 0): # if visited array value is zero then increase element because we get it first tym..
            ele +=1
        vis[pair[right][1]] +=1
        right +=1

    ## once we hit the window size calculate the answer..
    ## right now pointing greater than one window size..
    ans = pair[right-1][0] - pair[left][0] ## subtract first element with right-1 index element

    ## check for remaining element if any..
    while (right < len(pair)):
        # check if element already visited using visited array decrease value of ele and visited array..
        if (vis[pair[left][1]] == 1):
            ele -=1
        vis[pair[left][1]] -=1
        left +=1        ## update window.. if we further get ans we not include left previous index..

        while(ele < n and right < len(pair)):
            if (vis[pair[right][1]] == 0): # if visited array value is zero then increase element because we get it first tym..
                ele +=1
            vis[pair[right][1]] +=1
            right +=1
        ## if again window size hit then we take the minimum diffrence..
        if (ele == n):
            ans = min(ans, pair[right-1][0] - pair[left][0])
        else:
            break
    return ans

## method2 --> using basic concept increase minimum height and decrease maximum height to get optimize solution..
def getMinDiff(arr, n, k):
    arr.sort()  #sorting the array
    ans=arr[n-1]-arr[0] #it's same as substracting an+k-(ao+k) or an-k-(a0-k)
    small = 0
    big = 0

    for i in range(1,n):    #trying to make each tower highest
        if arr[i]>=k:
            small=min(arr[0]+k,arr[i]-k)    #finding minimum tower height
            big=max(arr[i-1]+k,arr[-1]-k)   #finding maximum tower height
            ans=min(ans,big-small)          #checking whether we get smaller value as result

    return ans


## Driver code...!!!!
if __name__ == "__main__":
    n,k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    print('minimum height between two building',getmindiff(arr,n,k))

'''
sample input..
4 2
1 5 8 10
'''
