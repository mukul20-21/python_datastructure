class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def  __str__ (self):
        result = []
        node = self.head                        # create a pointer named as node for over convience..!!
        while node:
            result.append(f'{node.data}')
            node = node.next
        return'-->'.join(result)
        
    def add_at_index(self,index,data):
        
        if  index <0:                                   # case1 where the index is less than zero, boundary cases..!!
            raise IndexError('Negative index is not a valid input..!!!')
        
        if  index == 0:                                  # case2 where the indez is zero or insert value at head...!!
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
            
        prev = None
        node = self.head
        counter = 0                                         # case3 in which index value is postive integer...!!!
        while node:                                     
            if  counter == index:
                new_node = Node(data)
                prev.next = new_node
                new_node.next = node
                return
            counter += 1
            prev = node
            node = node.next
        
        if  counter == index:                        # case4 where index is greater than the length of list
            new_node = Node(data)
            prev.next = new_node
        else:
            raise IndexError("Index can't greater than the length of list")
            
            
linked_list = LinkedList()
print(linked_list)
linked_list.add_at_index(0,1)                               # index function take two argument (index,data)...!!!!     
print(linked_list)
linked_list.add_at_index(1,2)                               # index function take two argument (index,data)...!!!!     
print(linked_list)
linked_list.add_at_index(1,3)                               # index function take two argument (index,data)...!!!!     
print(linked_list)
