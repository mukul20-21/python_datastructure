class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None
        
    def __str__(self):
        res = []
        temp = self.head
        while temp:
            res.append(f"{temp.data}")
            temp = temp.next
        return "-->".join(res)
    
    def add_last(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newnode
    
    
    def remove_loop(self,head):
        s = set()
        curr = head
        prev = None
        
        while curr:
            if curr not in s:
                s.add(curr)
                prev = curr
                curr = curr.next   
            else:
                prev.next = None
                break
                
## Driver code...!!!!llist = LinkedList()
llist = LinkedList()
llist.add_last(50)
llist.add_last(20)
llist.add_last(15)
llist.add_last(4)
llist.add_last(10)

 
# Create a loop for testing
llist.head.next.next.next.next.next = llist.head.next.next
 
llist.remove_loop(llist.head)
 
print ("Linked List after removing loop",llist)
 