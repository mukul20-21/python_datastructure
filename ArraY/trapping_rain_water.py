## how to calculate water trapper at particular index...
## water_trapper = min(left_max_building,right_max_building)-curr_height_building

## method1 --> Brute force take time --> O(N^2)

## Method2 --> Using prefix and suffix maximum sum.. time --> O(N) and space-->O(N)
def findwater(arr):
    n = len(arr)
    prefix = [0]*(n)        ## store prefix maximum sum from left to right [1...n-1]
    suffix = [0]*(n)        ## store suffix maximum sum from right to left [n-2...0]
    result = 0

    ## create prefix summ...
    prefix[0] = arr[0]
    for i in range(1,n):
        prefix[i] = max(prefix[i-1] , arr[i])

    ##create suffix summ...
    suffix[n-1] = arr[n-1]
    for i in range(n-2,-1,-1):
        suffix[i] = max(suffix[i+1] , arr[i])

    ## Calculate water_trap...
    for i in range(0,n):
        result += min(prefix[i],suffix[i]) - arr[i]

    return result

## Method3--> using two pointer approach.. time-->O(N) and space-->O(1)
def findwater(height):
    n = len(height)
    left = 0
    right = n-1
    maxleft = 0
    maxright = 0
    res = 0
    while (left<=right):
        if (height[left] <= height[right]):
            if (height[left] >= maxleft):
                maxleft = height[left]
            else:
                res += maxleft - height[left]
            left +=1
        else:
            if(height[right] >= maxright):
                maxright = height[right]
            else:
                res += maxright - height[right]
            right -=1
    return res

## Driver code...!!!!
if __name__ == "__main__":
    arr = list(map(int,input().split()))
    print(findwater(arr))
