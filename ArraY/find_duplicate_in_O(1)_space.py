## using hashing ..
def duplicates_hash(arr, n):

    s = dict()
    for i in range(n):
        if arr[i] in s:
            s[arr[i]] = s[arr[i]]+1
        else:
            s[arr[i]] = 1

    res = []
    for i in s:
        if s[i] > 1:
            res.append(i)

    if len(res)>0:
        return res
    else:
        return -1

## using given array as hashmap because in question it is given that range of array -->[1,length of array]
def duplicates_arr(arr, n):

    res = []

    for i in range(n):
        arr[arr[i]%n] = arr[arr[i]%n] + n

    for i in range(n):
        if (arr[i]//n>1):
            res.append(i)

    return res

## Driver code...!!!!1
if __name__ == "__main__":
    n = int(input())
    arr1 = list(map(int,input().split()))
    print('using array',duplicates_arr(arr1.copy(),n)) ## pass copy of main input array..
    print('using hashmap',duplicates_hash(arr1,n))
'''
sample input
5
2 3 1 2 3
'''
