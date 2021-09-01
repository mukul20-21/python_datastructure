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
    
    def removeDuplicates(self,head):
    
        temp = head
        if temp is None:
            return None
        while temp.next:
            if temp.data == temp.next.data:
                temp.next = temp.next.next
            else:
                temp = temp.next
    
        return head
    
if __name__ == "__main__":
    obj = Linkedlist()
    obj.add_last(1)
    obj.add_last(2)
    obj.add_last(2)
    obj.add_last(3)
    obj.add_last(4)
    obj.add_last(5)
    
    print(obj)
    obj.removeDuplicates(obj.head)
    print(obj)