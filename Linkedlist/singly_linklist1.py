# create nodes
# create linkedlist
# add nodes to linkedlist
# print linked-list

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        
    def  insert (self,newnode):
        if self.head is None:
            self.head = newnode
        else:
            lastnode = self.head
            while True:
                if lastnode is None:
                    break
                lastnode = lastnode.next
            lastnode.next = newnode
            
    def printlist(self):
        if self.head is None:
            print("Current list is empty...!!!")
            return
        currentnode = self.head
        while True:
            if currentnode is None:
                break
            print(currentnode.data)
            currentnode = currentnode.next

firstnode = node("mukul")

linkedlist = Linkedlist()
linkedlist.insert(firstnode)

#secondnode = node("cool")
#linkedlist.insert(secondnode)

Linkedlist.printlist()