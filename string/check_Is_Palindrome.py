'''
Given a string S, check if it is palindrome or not.
'''
#method1 --> using list slicing/reverse function..
def ispalindrome(S):
    rev = S[::-1]
    if S = rev:
        return 1
    else:
        return 0

## Method2 --> Compare ith element with nth index..
def ispalindrome(S):
    n = len(S)
    for i in range(0,len(S)//2):
        if S[i] != S[n-i-1]:
            return 0

    return 1

## Driver code...!!!!
if __name__ == "__main__":
    S = input()
    print('check if it is palindrome or not...',ispalindrome(S))
