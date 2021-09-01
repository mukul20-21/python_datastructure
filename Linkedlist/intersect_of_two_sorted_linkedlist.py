## here we get the new linkedlist as a result...

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Linkedlist:
    def __init__(self):
        self.head = None
            
    def insert(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
        else:
            temp = self.head
            while temp.next :
                temp = temp.next
            temp.next = newnode
    
    def findIntersection(self,head1,head2):
    #return head
        l1 = head1
        l2 = head2
        head = None
        curr = None
    
        while l1 and l2:
            if (l1.data == l2.data):
                if head == None:
                    temp = Node(l1.data)
                    head = temp
                    curr = temp
                else:
                    temp = Node(l1.data)
                    curr.next = temp
                    curr = curr.next
                l1 = l1.next
                l2 = l2.next
        
            else:
                if (l1.data < l2.data):
                    l1 = l1.next
                else:
                    l2 = l2.next
        
        return head

def printlist(head):
    res = []
    temp = head
    while(temp):
        res.append(f"{temp.data}")
        temp = temp.next
    return "-->".join(res)

## Driver code...!!!!
            
if __name__ == "__main__":
    first = Linkedlist()
    second = Linkedlist()
    ## first linkedlist
    first.insert(1)
    first.insert(2)
    first.insert(4)
    first.insert(6)
    first.insert(8)
    ## second linkedlist
    second.insert(1)
    second.insert(2)
    second.insert(6)
    second.insert(7)
    
    print("list1-->>",printlist(first.head))
    print("list2-->>",printlist(second.head))
    
    final = Linkedlist()
    out = None
    out = final.findIntersection(first.head,second.head)
  
    
    print("after intersection final list-->",printlist(out))