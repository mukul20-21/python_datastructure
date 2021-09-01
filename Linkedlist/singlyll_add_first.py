class node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def  __init__(self):
        self.head = None
    
    def  __str__(self):
        result = []
        node = self.head                                    # declare a variable as node it is not the class node declare above..!!
        while node:                                         # run untill node.next -> points to none value..!!
            result.append(f'{node.data}')
            node = node.next
        return '-->'.join(result)
        
    def  add_first(self,data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node
        
linked_list = LinkedList()
print(linked_list,"Empty list because we just initialize the linked_list")                                              # here __str__ function calls automatically..!!!    

linked_list.add_first(1)
print(linked_list)
linked_list.add_first(2)
print(linked_list)
linked_list.add_first(3)
print(linked_list)