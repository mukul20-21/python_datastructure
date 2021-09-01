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
      

def countPairs(first, second, value):
    count = 0
    while (first != second and second.next != first):
        
        if ((first.data + second.data) == value):
            count += 1
            first = first.next
            second = second.prev
        
        elif ((first.data + second.data) > value):
            second = second.prev
        else:
            first = first.next
 
    return count
 
# Function to count triplets in a sorted doubly linked list whose sum is equal to a given value 'x'
def countTriplets(head, x):
     
    if (head == None):
        return 0
 
    current = head
    first = None
    last = None
    count = 0
 
    # Get pointer to the last node of the doubly linked list
    last = head
     
    while (last.next != None):
        last = last.next
 
    # Traversing the doubly linked list
    while current != None:
 
        # start from second node while keeping first fix
        first = current.next
 
        # count pairs with sum(x - current.data) in the range first to last and add it to the 'count' of triplets
        count = count + countPairs(first, last, x - current.data)
        current = current.next
    return count

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
        

## Driver code...!!!!!
if __name__ == "__main__":
    head = None
    head = insert(head,1)
    head = insert(head,2)
    head = insert(head,4)
    head = insert(head,5)
    head = insert(head,6)
    head = insert(head,8)
    head = insert(head,9)
    
    print(printlist(head))
    x = 17 
    print("Count no of triplets =",countTriplets(head, x))

'''
## function to print the node and reverse of linkedlist.. 

def printlist(node):
    last = None
    print("Traversal in forward direction ")
    while (node != None):
        print(node.data, end=" ")
        last = node
        node = node.next
 
    print("\nTraversal in reverse direction ")
    while (last != None):
        print(last.data, end=" ")
        last = last.prev
'''  