class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
	
    def  print_list(self,head):
        res = []
        temp = head
        while temp:
            res.append(f"{temp.data}")
            temp = temp.next
        return '-->'.join(res)
	
	
    def add_last(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newnode
	
    def reverse_list(self,head,k):
        if self.head is None:
            return
        
        temp = head
        nextt = None
        prev = None
        c = 0
        while temp!= None and c < k:
            nextt = temp.next
            temp.next = prev
            prev = temp
            temp = nextt
            c += 1
        
        # condition to recursive call for same function to link prev node after reverse..
        if nextt != None:
            head.next = self.reverse_list(nextt,k)
        return prev
			
		

## Driver code..!!!!
if __name__ == "__main__":
    obj = Linkedlist()
    obj.add_last(1)
    obj.add_last(2)
    obj.add_last(3)
    obj.add_last(4)
    obj.add_last(5)
    obj.add_last(6)
    obj.add_last(7)
    obj.add_last(8)
    
    print("before reverse",obj.print_list(obj.head))
    k = 3
    
    head_new =  obj.reverse_list(obj.head,k)
    print("after reverse",obj.print_list(head_new))
	
	
	