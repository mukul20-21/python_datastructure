class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def isPalindrome(head):
        #code here
    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        
    curr = slow
    nextt = None
    prev = None
    
    while curr != None:
        nextt = curr.next
        curr.next = prev
        prev = curr
        curr = nextt
    
    last = prev
    front = head
        
    while last:
        if last.data != front.data:
            return False
        last = last.next
        front = front.next
        
    return True
    
## Driver code..!!!
    head = Node(5)
    head.next = Node(4) 
    head.next.next = Node(3)
    head.next.next.next = Node(2)
    head.next.next.next.next = head
    
    if isPalindrome(head):
        print("it is a palindromic linkedlist")
    else:
        print("Not a palindromic list")