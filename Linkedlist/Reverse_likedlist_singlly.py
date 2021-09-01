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
	
	def reverse_list(self):
		if self.head is None:
			return
		temp = self.head
		prev = None
		while temp is not None:
			nextt = temp.next
			temp.next = prev
			prev = temp
			temp = nextt
		self.head = prev
			
		

## Driver code..!!!!
if __name__ == "__main__":
	obj = Linkedlist()
	obj.add_last(1)
	obj.add_last(2)
	obj.add_last(3)
	obj.add_last(4)
	obj.add_last(5)
	obj.add_last(6)
	print("before reverse",obj)
	obj.reverse_list()
	print("after reverse",obj)
	
	
	