## shift array by one and insert new value at start index..
def rotate(arr,n):
    temp = arr[n-1]
    for i in range(n-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = temp
    return arr

## Driver code...!!!!
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split()))
