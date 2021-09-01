def mini_jump(arr,n):    
    maxR = arr[0]
    step = arr[0]
    jump = 1

    if (n==1):
        return 0
    elif(arr[0] == 0):
        return -1
    else:
        for i in range(1,n):
            if (i == n-1):
                return jump
            maxR = max(maxR, arr[i]+i)
            step -=1
            if(step==0):
                jump+=1
            ## update step value after getting maxi reach..
                if (i>=maxR):
                    return -1

                step = maxR - i

## Driver code...!!!!
if __name__ == "__main__":
    N = int(input())
    arr = list(map(int,input().split()))

'''
sample input...
11
1 3 5 8 9 2 6 7 6 8 9
'''
