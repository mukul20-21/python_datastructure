def reverse_arr(arr):
    start = 0
    end = len(arr)-1
    while start<end:
        arr[start],arr[end] = arr[end],arr[start]
        start +=1
        end -=1
    return arr

## Reverse a string using slicing or using for loop with extra space...
'''
def reverse(s):
    return s[::-1]

def reverse(s):
    rev = ""
    for i in range(len(s)-1,-1,-1):
       rev += s[i]

    return rev
'''

## diver code...!!!!
if __name__ == "__main__":
    arr = list(map(int,input().split()))
    print('reverse a array using swapping variable-->',reverse_arr(arr))
