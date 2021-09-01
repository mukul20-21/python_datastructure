class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Linkedlist:
    def __init__(self):
        self.head = None
	
    def add_last(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newnode
    
    def detect_loop(self,head):
        slow = head
        fast = head
        while(slow and fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

## Driver Code..!!!

if __name__ == "__main__":
    obj = Linkedlist()
    obj.add_last(1)
    obj.add_last(2)
    obj.add_last(3)
    obj.add_last(4)
    
    obj.head.next.next.next.next = obj.head
    
    if obj.detect_loop(obj.head):
        print("LOOP present")
    else:
        print("Not detected")
                