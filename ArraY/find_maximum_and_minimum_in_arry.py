def find_min_max(arr):
    #your code here

    if len(arr) == 1:
        mn = arr[0]
        mx = arr[0]
        return mn,mx

    # If there are more than one elements, then initialize min and max
    if arr[0] > arr[1]:
        mx = arr[0]
        mn = arr[1]
    else:
        mx = arr[1]
        mn = arr[0]

    for i in range(2, len(arr)):
        if arr[i] > mx:
            mx = arr[i]
        elif arr[i] < mn:
            mn = arr[i]

    return mn,mx

## Driver code...!!!
if __name__ == "__main__":
    arr = list(map(int,input().split()))
    print(find_min_max(arr))
