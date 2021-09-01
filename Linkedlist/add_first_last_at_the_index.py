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
			res.append(f'{temp.data}')
			temp = temp.next
		return '->'.join(res)

	def add_first(self,data):
		newnode = Node(data)
		newnode.next = self.head 		## initial head pointer consist null value..
		self.head = newnode
	
	def add_last(self,data):
		newnode = Node(data)
		if self.head is None:
			self.head = newnode
		else:
			temp = self.head
			while temp.next:
				temp = temp.next
			temp.next = newnode

	def add_at_index(self,index,data):
		# for negative index
		if index < 0:
			raise IndexError('Negative index is not valid index')
		## if index == 0..
		if index == 0:
			newnode = Node(data)
			newnode.next = self.head
			self.head = newnode
			return
		
		## If index positive
		prev = None
		temp = self.head
		counter = 0
		while temp:
			if counter == index:
				newnode = Node(data)
				prev.next = newnode
				newnode.next = temp
				break
			counter+=1
			prev = temp
			temp = temp.next
			
		## if index is not present in list...
		else:
			raise IndexError("Index is not present")
			
			

## Driver code..!!!!
if __name__ == "__main__":
	llobj = Linkedlist()
	print("Empty list",llobj)
	llobj.add_first(1)
	print(llobj)
	llobj.add_first(2)
	print(llobj)
	llobj.add_last(3)
	print(llobj)
	llobj.add_last(4)
	print(llobj)
	llobj.add_at_index(0,11)
	print(llobj)
	llobj.add_at_index(2,12)
	print(llobj)
	llobj.add_at_index(3,17)
	print(llobj)
	