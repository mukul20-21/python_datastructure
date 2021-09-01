class Node: 
	def __init__(self,data): 
		self.data = data 
		self.next = None

def push(head, data): 
	if not head: 
		return Node(data) 
 
	newNode = Node(data) 
	newNode.next = head  
	head = newNode 
	return head 

def circular(head): 
    start = head 
	while(head.next is not None): 
		head = head.next
        
	head.next = start 
	return start 
 
def displayList(node): 
	start = node 
	while(node.next is not start): 
		print("{} ".format(node.data),end="") 
		node=node.next 
	print("{} ".format(node.data),end="") 

# Driver Code 
if __name__=='__main__': 
	 
	head=None

	head=push(head,15) 
	head=push(head,14) 
	head=push(head,13) 
	head=push(head,22) 
	head=push(head,17) 
 
	circular(head) 
	print("Display List:") 
	displayList(head) 
 
