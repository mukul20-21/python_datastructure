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
    
    def __str__(self):
        res = []
        temp = self.head
        while temp:
            res.append(f"{temp.data}")
            temp = temp.next
        return "-->".join(res)
    
    
    def detect_loop(self,head):
        if head == None or head.next == None:
            return None
        
        slow = head
        fast = head
        
        while(slow and fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        if slow != fast:  # if loop not exist..
            return None
        
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow
## Driver Code..!!!

if __name__ == "__main__":
    obj = Linkedlist()
    obj.add_last(1)
    obj.add_last(2)
    obj.add_last(3)
    obj.add_last(4)
    obj.add_last(5)
    
    print(obj)
    obj.head.next.next.next.next.next = obj.head.next
    res = obj.detect_loop(obj.head)
    if res:
        print("LOOP start at node", res.data)
    else:
        print("Loop not exist at all")
       
                