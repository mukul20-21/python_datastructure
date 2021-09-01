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
     
    def  delete_index(self,index):
        prev = None
        node = self.head
        while node and index:                               # slighty change then previous their we contrain on key value...
            prev = node
            node = node.next
            index -= 1
        if  node:
            if prev:
                prev.next = node.next
            else:
                self.head = node.next
        else:
            raise('enter index is greater than the length of linked_list...!!!')
            
linked_list = LinkedList([1,2,3])
print(linked_list)

linked_list.delete_index(1)
print(linked_list)
linked_list.delete_index(0)
print(linked_list)
