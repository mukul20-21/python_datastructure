#Function to check whether there is a subarray present with 0-sum or not.
def subArrayExists(arr,n):
    ##Your code here
    summ = 0
    s = set()

    for i in range(n):
        summ += arr[i]

        # If prefix sum is 0 or
        # it is already present
        if summ == 0 or summ in s:
            return True
        s.add(summ)

    return False

## Driver code...!!!
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int,input().split()))
    print(subArrayExists(arr,n))
