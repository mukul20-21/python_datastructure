class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
def printlist(head):
    res = []
    temp = head
    while temp:
        res.append(f"{temp.data}")
        temp = temp.next
    return "-->".join(res)

def mergesort(head):
    first = None
    second = None
    
    if (head == None or head.next == None):
        return head
    
    mid = findmiddle(head)
    first = head
    second = mid.next
    mid.next = None
    left = mergesort(first)
    right = mergesort(second)
    final_head = mergeboth(left,right)
    return final_head
    
def mergeboth(first,second):
    ans = None
    
    if not first:
        return second
    if not second:
        return first
    
    if (first.data <= second.data):
        ans = first
        ans.next = mergeboth(first.next,second)
    else:
        ans = second
        ans.next = mergeboth(first,second.next)
    
    return ans

def findmiddle(head):
    slow = head
    fast = head.next
    
    while (fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next
    
    return slow
    
## Driver code...!!!
head = Node(5)
head.next = Node(4)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)

print("before sorting",printlist(head))
head = mergesort(head)
print("after sorting",printlist(head))
    