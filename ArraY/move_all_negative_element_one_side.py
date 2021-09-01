## function use partition process of quick sort...
# here we assume pivot == 0.
def negative_element(arr):
    pivot = 0
    i = -1
    for j in range(len(arr)):
        if arr[j]<pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
        elif arr[j]>=pivot:
            j+=1
    return arr

## function use two pointer approach left = 0 and right = n-1

def negative_ele(arr):
    left = 0
    right = len(arr)-1
    while left<=right:
        if arr[left]>0 and arr[right]>0:        ## if both element is positive..
            right -=1
        elif arr[left]<0 and arr[right]<0:      ## if both element is negative..
            left +=1
        elif arr[left]>0 and arr[right]<0:      ## if left --> positive and right --> negative..
            ## swap the element..
            arr[left],arr[right] = arr[right],arr[left]
            left+=1
            right-=1
        else:                                   ## if left--> negative and right --> positive..
            left +=1
            right -=1
    return arr

## Driver code...!!!
if __name__ == "__main__":
    arr = list(map(int,input().split()))
    ## both function take O(N) time and constant space...!!!!
    print("before function call-->",arr)
    print()
    print("Partition process-->",negative_element(arr))
    print("Two pointer approach-->",negative_ele(arr))

'''
sample input...
-1 2 7 0 9 -13 -12 1 21
'''
