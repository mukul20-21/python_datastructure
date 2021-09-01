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
        
    def  delete_key(self , key):
        prev = None
        node = self.head
        while node and (node.data != key):
            prev = node
            node = node.next
        if node:                                # run for (node.data != key ) condition... it further divide into two step... delete the first node or between node..!!
            if prev:
                prev.next = node.next
            else:
                self.head = node.next
            del node
        else:
            raise ValueError('key not found which you want to delete in list...!!!')
      
      
linked_list = LinkedList([1,2,3])              # enter value at the time of construtor creator...
print(linked_list)

linked_list.delete_key(2)
print(linked_list)
linked_list.delete_key(3)
print(linked_list)
linked_list.delete_key(1)
print(linked_list)
