class node:
    def __init__(self,data):
        self.data = data
        self.next = None
     
class LinkedList:
    def __init__(self):
        self.head = None
    
    def __str__(self):
        result = []
        node = self.head
        while node:
            result.append(f'{node.data}')
            node = node.next
        return '-->'.join(result)
        
    def add_last(self,data):
        new_node = node(data)
        if self.head:
            last = self.head
            while last.next:                    # used to take last pointer to last node contain none value..!!
                last = last.next
            last.next = new_node
        else:
            self.head = new_node

linked_list = LinkedList()
print(linked_list)

linked_list.add_last(1)
print(linked_list)

linked_list.add_last(2)
print(linked_list)

linked_list.add_last(3)
print(linked_list)
                        
        