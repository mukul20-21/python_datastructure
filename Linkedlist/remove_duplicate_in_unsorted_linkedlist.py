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
    
    def remove_duplicate(self,head):
        curr = head
        store = {} ## Store node into map...
        store[curr.data] = 1
        prev = curr
        curr = curr.next
        
        while curr != None:

            if curr.data in store:
                prev.next = curr.next
            else:
                store[curr.data] = 1
                prev = curr
            curr = curr.next
        
        return head
        
## driver code...!!!

if __name__ == "__main__":
    obj = Linkedlist()
    obj.insert(1)
    obj.insert(2)
    obj.insert(3)
    obj.insert(2)
    obj.insert(4)
    obj.insert(5)
    obj.insert(4)
    
    print("before remove element",obj)
    obj.remove_duplicate(obj.head)
    print("after remove element",obj)
    