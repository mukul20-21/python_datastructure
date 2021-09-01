class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class Doubly_Linked_List:
    
    def __init__(self):
        self.head = None
    
    def __str__(self):
        result = []
        node=self.head
        while node:
            result.append(f'{node.data}')
            node = node.next
        return '->'.join(result)
    
    def append_list(self,data):
        newnode = node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newnode
            newnode.prev = current
            newnode.next = None
        else:
            self.head = newnode
            newnode.prev = None
            
    def prepend_list(self,data):
        newnode = node(data)
        if self.head:
            self.head.prev = newnode
            newnode.next = self.head
            self.head = newnode
            newnode.prev = None
        else:
            newnode.prev = None
            self.head = newnode
    
doubll = Doubly_Linked_List()
print('till list is empty',doubll)

doubll.prepend_list(0)
print(doubll)
doubll.append_list(1)
print(doubll)
doubll.append_list(2)
print(doubll)
doubll.append_list(3)
print(doubll)
doubll.append_list(4)
print(doubll)
doubll.prepend_list(5)
print(doubll)