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

    def reverse(self,head):
        prev = None
        nex = None
        curr = head
        while curr != None:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        return prev
        
    def add_one_at_edd(self,head):
        head = self.reverse(head)
        curr = head
        f = True
        while curr != None and f == True:
            ## corner case... last element == 9 and one extra zero at starting of linkedlist in O(1) time
            if (curr.next == None and curr.data == 9):
                curr.data = 1
                temp = Node(0)
                temp.next = head
                head = temp
                curr = curr.next ## for breaking of loop
            
            elif curr.data == 9:  
                curr.data = 0
                curr = curr.next
            
            else:
                curr.data = curr.data + 1
                curr = curr.next
                f = False   # condition to break while loop
        
        head = self.reverse(head)
        return head
                

## Driver code...
if __name__ == "__main__":
    obj = Linkedlist()
    obj.insert(1)
    obj.insert(9)
    obj.insert(9)
    obj.insert(9)
    print("before adding 1 in linkedlist",obj)
    obj.add_one_at_edd(obj.head)
    print("after adding 1 in linkedlist", obj)