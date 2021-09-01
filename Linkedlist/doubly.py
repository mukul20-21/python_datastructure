class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Linkedlist:
    def  __init__(self):
        self.head = None
        
    def  __str__(self):
        result = []
        node = self.head
        while node:
            result.append(f'{node.data}')
            node = node.next
        return '->'.join(result)
        
    def  add_first (self,data):
        newnode = node(data)
        newnode.next = self.head
        self.head = newnode
        
        
linked_list = Linkedlist()
print(linked_list)

linked_list.add_first(1)
print(linked_list)
linked_list.add_first(2)
print(linked_list)
linked_list.add_first('third_element')
print(linked_list)
linked_list.add_first('4th_element')
print(linked_list)