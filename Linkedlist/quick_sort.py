class Node:
	def __init__(self, val):
		self.data = val
		self.next = None

''' takes first and last node,but do not break any links in the whole linked list'''
def paritionLast(start, end):
    if (start == end or start == None or end == None):
        return start

    pivot_prev = start
    curr = start
    pivot = end.data

    '''iterate till one before the end, no need to iterate till the end because end is pivot'''
    while (start != end):
        if (start.data < pivot):
			# keep tracks of last modified item
            pivot_prev = curr
            temp = curr.data
            curr.data = start.data
            start.data = temp
            curr = curr.next
        start = start.next

    temp = curr.data
    curr.data = pivot
    end.data = temp
    ''' return one previous to current because current is now pointing to pivot '''
    return pivot_prev

def sort(start, end):
    if(start == None or start == end or start == end.next):
        return

    # split list and partion recurse
    pivot_prev = paritionLast(start, end)
    sort(start, pivot_prev)

    # if pivot is picked and moved to the start,that means start and pivot is same so pick from next of pivot'''
    if(pivot_prev != None and pivot_prev == start):
        sort(pivot_prev.next, end)

    # if pivot is in between of the list,start from next of pivot, since we have pivot_prev, so we move two nodes
    elif (pivot_prev != None and pivot_prev.next != None):
        sort(pivot_prev.next.next, end)

def printlist(head):
    res = []
    temp = head
    while temp:
        res.append(f"{temp.data}")
        temp = temp.next
    return "-->".join(res)

if __name__ == "__main__":

    head = Node(5)
    head.next = Node(4) 
    head.next.next = Node(3)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(1)
	

    n = head
    while (n.next != None):
        n = n.next

    print("Linked List before sorting",printlist(head))
    sort(head, n)
    print("\nLinked List after sorting",printlist(head))
	
	