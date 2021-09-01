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

def insert(head,data):
    newnode = Node(data)
    if head is None:
        head = newnode
    else:
        temp = head
        while temp.next :
            temp = temp.next
        temp.next = newnode
    return head

def sortedlist(head):
    count = [0, 0, 0]
    ptr = head
    while ptr != None:
        count[ptr.data]+=1
        ptr = ptr.next
 
    i = 0
    ptr = head
    
    while ptr != None:
        if count[i] == 0:
            i+=1
        else:
            ptr.data = i
            count[i]-=1
            ptr = ptr.next
        
    return head
 
 ## driver code...!!!
if __name__ == "__main__":
    head = None
    head = insert(head,2)
    head = insert(head,1)
    head = insert(head,0)
    head = insert(head,2)
    head = insert(head,1)
    head = insert(head,0)
    head = insert(head,1)
    
    print("before sort",printlist(head))
    sortedlist(head)
    print()
    print("after sort",printlist(head))
    
 