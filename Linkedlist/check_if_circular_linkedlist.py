class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def check_list(head):
    if head==None:
        return 1
    temp = head.next
    while temp != None and temp != head:
        temp = temp.next
    
    if temp == head:
        return True
    else:
        return False

## Driver code...!!!!
if __name__ == "__main__":
    head = Node(5)
    head.next = Node(4) 
    head.next.next = Node(3)
    head.next.next.next = Node(2)
    head.next.next.next.next = head
    
    if check_list(head):
        print("loop present")
    else:
        print("Loop not present")