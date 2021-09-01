## this function use set datastructure take time-->O(N) to get kth smallest element...
def k_smallest(arr,k):
    s = set(arr)
    item = 0
    for i in range(k):
        item = min(s)
        s.remove(min(s))
    return temp

## using heap --> import heapq take time-->O(N + KlogN)
## for heapify --> )O(LogN)
## for binary heap creation take --> O(N) time..
from heapq import heappush,heappop,heapify
def kth_element(arr,k):
    heapify(arr)
    item = 0
    for i in range(k):
        item = heappop(arr)
    return item


##Driver Code...!!!!
if __name__ == "__main__":
    k = int(input())
    arr = list(map(int,input().split()))
    print('kth_smallest_element-->',kth_element(arr,k))
