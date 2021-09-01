class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def printlist(head):
    res = []
    temp = head
    while temp:
        res.append(f"{temp.data}")
        temp = temp.next
    return "<-->".join(res)

def insert(head,data):
    newnode = Node(data)
    if head is None:
        head = newnode
        head.prev = None
    else:
        last = head
        while last.next != None:
            last = last.next
        last.next = newnode
        newnode.prev = last
    return head
        

def rotate(head,N):
    
    if N == 0 :
        return

    current = head
    count = 1
    while count < N and current != None :
        current = current.next
        count += 1
 
    if current == None :
        return
 
    NthNode = current
 
    while current.next != None :
        current = current.next
 
    current.next = head
    head.prev = current
    head = NthNode.next
    head.prev = None
    NthNode.next = None
 
    return head

## Driver code...!!!!!
if __name__ == "__main__":
    head = None
    head = insert(head,1)
    head = insert(head,2)
    head = insert(head,3)
    head = insert(head,4)
    head = insert(head,5)
    head = insert(head,6)
    head = insert(head,7)
    
    print(printlist(head))
    n = 4 
    head = rotate(head, n)
    print()
    print(printlist(head))