class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def printlist( head):
    temp = head
    res = []
    while(True) :
        res.append(f"{temp.data}")
        temp = temp.next
        if (temp == head):
            break
    return "-->".join(res)

def deleteNode( head, key) :
    if (head == None):
        return
          
    # If the list contains only a single node
    if((head).data == key and (head).next == head):
        head = None
    last = head
    d = None
      
    # If head is to be deleted
    if((head).data == key) :
          
        # Find the last node of the list
        while(last.next != head):
            last = last.next
              
        # Point last node to the next of head i.e. the second node of the list
        last.next = head.next
        head = last.next
      
    # Either the node to be deleted is not found or the end of list is not reached
    while(last.next != head and last.next.data != key) :
        last = last.next
  
    # If node to be deleted was found
    if(last.next.data == key) :
        d = last.next
        last.next = d.next
      
    else:
        return -1
      
    return head

## Driver code..!!!
if __name__ == "__main__": 
    head = Node(5)
    head.next = Node(4) 
    head.next.next = Node(3)
    head.next.next.next = Node(2)
    head.next.next.next.next = head
    
    print("before deletion",printlist(head))
    
    head = deleteNode( head, 3) 
    
    print("after deletion",printlist(head))
    