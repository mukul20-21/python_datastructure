'''
Function to reverse string inplace avoid extra space..
Not return any function jst reverse the string..
function take list with str element..
'''
#method1 --> using_reverse function...
def reverse(S):
    S.reverse()

##Method2 --> using list slicing...
def reverse(S):
    temp = S[::-1]
    for i in range(len(S)):
        S[i] = temp[i]

'''
Method3 --> Using Two pointers--->
                                -- Iterative solution

                                --Recursive solution.
'''
## Iterative method...
def reverse(S):
    left = 0
    right = len(S)-1
    while left<right:
        S[left],S[right] = S[right],S[left]
        left +=1
        right -=1

## Recursive Method..
def reverse(S):

    def helper(left,right):
        if left<right:
        S[left],S[right] = S[right],S[left]
        helper(left+1,right-1)

    ## function call..
    helper(0,len(S)-1)    

## Driver Code...!!!!
if __name__ == "__main__":
    S = list(input().split())
    reverse(S)
    print('string after reverse...',S)
