## method1 --> sort the array and cnt the number of element are consecutive subsequence..
## time --> O(NLogN)
def findLCS(arr, N):

    ans = 0
    count = 0
    arr.sort()
    v = []
    v.append(arr[0])

    # Insert repeated elements only once in the vector
    for i in range(1, n):
        if (arr[i] != arr[i - 1]):
            v.append(arr[i])

    # Find the maximum length by traversing the array
    for i in range(len(v)):
        # Check if the current element is equal to previous element +1
        if (i > 0 and v[i] == v[i - 1] + 1):
            count += 1
        # Reset the count
        else:
            count = 1
        # Update the maximum
        ans = max(ans, count)

    return ans

#method2 --> using hashset--it take O(1) time for searching...
'''
Approach...
step1--> insert all element into set
step2 --> iterate on set & check(curr_value-1) element present or not..
            --If present move forward
            --Else store value and exit loop

step3--> Again update store value & simanteously update counter value..
            --If store_value+1 present in set update store value by 1 and also update cnt..
            --If not present, jst store max of cnt value & exit..
'''

def findLCS(arr):
    hashset = set()
    for i in arr:       # step1
        hashset.add(i)

    mx_cnt = 0
    for i in arr:
        if i-1 not in hashset:   ## Step2
            curr_ele = i
            curr_cnt = 1

            while curr_ele+1 in hashset:   ## step3
                curr_ele +=1
                curr_cnt +=1
            mx_cnt = max(mx_cnt,curr_cnt)

    return mx_cnt

## Driver code...!!!!
if __name__ == "__main__":
    arr = list(map(int,input().split()))
    print('print cnt of longest consicutive subsequence-->',findLCS(arr))

'''
sample input...
5 4 3 2 1
'''
