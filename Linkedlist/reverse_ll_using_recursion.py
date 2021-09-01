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
            
    def reverse(head):
        # If head is empty or has reached the list end
        if head is None or head.next is None:
            return head
 
        # Reverse the rest list
        rest = self.reverse(head.next)
 
        # Put first element at the end
        head.next.next = head
        head.next = None

        # Fix the header pointer
        return rest
 

## Driver code...!!!
 
if __name__ == "__main__":
	obj = Linkedlist()
	obj.add_last(1)
	obj.add_last(2)
	obj.add_last(3)
	obj.add_last(4)
	obj.add_last(5)
	obj.add_last(6)
	print("before reverse",obj)
	obj.reverse(Linkedlist.head)
	print("after reverse",obj)
	