class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Linkedlist:
    def __init__(self):
        self.head = None
    
    def __str__(self):
        res = []
        temp = self.head
        while temp:
            res.append(f"{temp.data}")
            temp = temp.next
        return "-->".join(res)
    
    
    def insert(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
        else:
            temp = self.head
            while temp.next :
                temp = temp.next
            temp.next = newnode
            
    def last_to_move(self):
        last = self.head
        sec_last = None
        while last and last.next:
            sec_last = last
            last = last.next
            
        sec_last.next = None
        last.next = self.head
        self.head = last
        
        
        #return head


## Driver Code...!!!!

if __name__ == "__main__":
    obj = Linkedlist()
    obj.insert(1)
    obj.insert(2)
    obj.insert(3)
    obj.insert(4)
    obj.insert(5)
    obj.insert(6)
    obj.insert(7)
    
    print("before move element",obj)
    obj.last_to_move()
    print("after move element last element",obj)