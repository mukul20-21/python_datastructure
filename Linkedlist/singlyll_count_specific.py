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
        
    def  count_specific(self):
        count = []
        node = self.head
        while node:
            count.append(node.data)
            node = node.next
        return len(set(count))
        
linked_list = LinkedList([1,2,2,3])
print(linked_list)
print(linked_list.count_specific())