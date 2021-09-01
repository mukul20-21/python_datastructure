## function take (O(N) + O(NLogN)) time overall time --> O(NlogN) is unsorted array is given...
def merge(intervals):
    intervals.sort()
    res = []
    if len(intervals)==0:
        return intervals
    temp = intervals[0]
    for i in intervals:
        if temp[1] >= i[0]:
            temp[1] = max(temp[1],i[1])
        else:
            res.append(temp)
            temp = i
    res.append(temp)
    return res

## Driver code...!!!!!
if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        temp = list(map(int,input().split()))
        arr.append(temp)
    print('before merge input list',arr)
    print()
    print('after merge-->',merge(arr))

'''
sample input..
4
1 3
2 6
8 10
15 18

'''
