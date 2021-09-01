class Node:
    def __init__(self , data):
        self.data = data
        self.next = None
        
class LinkedList:
    
    def  __init__(self , array):                                # initialize the head pointer along with enter element in list using for loop...!!! reverse array due to insert at beginning...
        self.head = None
        for element in array[::-1]:
            new_node = Node(element)
            new_node.next = self.head
            self.head = new_node
    
    def  __str__(self):
        result = []
        node = self.head
        while node:
            result.append(f'{node.data}')
            node = node.next
        return '-->'.join(result)
        
    def  display_circular(self):
        node = self.head
        while  node.next is not None:
            node = node.next
        node.next = self.head
        return node
        
        
    
    
linked_list = LinkedList([1,2,3,4])
print(linked_list)
print("circular linked_list ,last node next points the self.head value at==>",linked_list.display_circular())