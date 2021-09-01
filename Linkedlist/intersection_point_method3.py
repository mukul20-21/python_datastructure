# Python3 implementation of the approach

# Link list node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# Function to get the intersection point
# of the given linked lists
def getIntersectionNode( head1, head2):

    curr1 = head1
    curr2 = head2

    # While both the pointers are not equal
    while (curr1 != curr2):

        # If the first pointer is None then set it to point to the head of the second linked list
        if (curr1 == None) :
            curr1 = head2
        
        # Else point it to the next node
        else:
            curr1 = curr1.next
        
        # If the second pointer is None then set it to point to the head of the first linked list
        if (curr2 == None):
            curr2 = head1
        
        # Else point it to the next node
        else:
            curr2 = curr2.next
        
    # Return the intersection node
    return curr1.data

def printlist(head):
    res = []
    temp = head
    while(temp):
        res.append(f"{temp.data}")
        temp = temp.next
    return "-->".join(res)


## Driver N
#newNode = None
head1 = Node(10)
#head1.data = 10
head2 = Node(3)

head2.next = Node(6)

head2.next.next = Node(9)
## link two linkedlist together..
newNode = Node(15)
head1.next = newNode
head2.next.next.next = newNode

newNode = Node(30)
head1.next.next = newNode
head1.next.next.next = None

print("list1",printlist(head1))
print("list2",printlist(head2))

# Print the intersection node
print( "intersection point in O(1) space-->",getIntersectionNode(head1, head2))

