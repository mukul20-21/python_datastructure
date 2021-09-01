'''
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

    countAndSay(1) = "1"
    countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.

To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character.
Then for each group, say the number of characters, then say the character. To convert the saying into a digit string, replace the counts with a number and concatenate every saying.

For example, the saying and conversion for digit string "3322251":

Given a positive integer n, return the nth term of the count-and-say sequence.
'''
'''
sample input...
Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
'''
#########
#Approach-->
'''
use temp variable and j pointer help to cnt previous element occurance and start iteration from 2 element.
        -- if s[j] == s[j-1]:
                -- jst update the cnt..
        -- else:
                store occurance
                store element for which we cnt its occurance into temp
        -- after complete internal loop given temp value again to outer loop for next n value in sequence..
'''

## Implemetation....
def countAndSay(n):
    if (n==1):
        return '1'
    if (n==2):
        return '11'
    s = '11'

    for i in range(3,n+1):
        temp = ""
        s = s + "&"         ## add symbol to differentiate b/w previous and current string..
        cnt = 1

        for j in range(1,len(s)):
            if (s[j] != s[j-1]):

                temp = temp + str(cnt)          ## add count of element
                temp = temp + s[j-1]            ## add element for which count no. of occurance..
                cnt = 1
            else:
                cnt +=1
        s = temp
    return s

## Driver code...!!!!
if __name__ == "__main__":
    n = int(input())
    print(countAndSay(n))
