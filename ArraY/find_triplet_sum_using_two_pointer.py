'''
Given an array arr of size n and an integer X. Find if there's a triplet in the array which sums up to the given integer X.
'''
## same question as-->check pair is present or not in array with given X value..
def find_triplet(A, n, X):
    A.sort()
    for i in range(n-2):
       #Taking two pointers. One at element after ith index and another at the last index.
        l=i+1
        r=n-1
        while(l<r):
            curr_sum=A[i]+A[l]+A[r]
            #If sum of elements at indexes i, l and r is equal to required number, we return true.
            if(curr_sum==X):
                return True
            #Else if the sum is less than required number, it means we need to increase the sum so we increase the left pointer l.
            elif(curr_sum<X):
                l+=1
            #Else the sum is more than required number and we need to decrease the sum so we decrease the right pointer r.
            else:
                r-=1

   #returning false if no triplet sum equal to required number is present.
    return False

## Driver code...!!!!
if __name__ == "__main__":
    n,X = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    print("triplet present with given X in array",find_triplet(arr,n,X))

'''
sample input...
Input:
n = 6, X = 13
arr[] = [1 4 45 6 10 8]
Output:1
Explanation: The triplet {1, 4, 8} in the array sums up to 13.
'''
