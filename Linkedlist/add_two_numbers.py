class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Linkedlist:
    def __init__(self):
        self.head = None
    
    def __str__(self):
        res = []
        temp = self.head
        while temp:
            res.append(f"{temp.data}")
            temp = temp.next
        return "-->".join(res)
    
   
            
    def insert(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
        else:
            temp = self.head
            while temp.next :
                temp = temp.next
            temp.next = newnode

    def reverse(self,head):
        prev = None
        nex = None
        curr = head
        while curr != None:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        return prev

    def addTwoLists(self, first, second):
        # code here
        first = self.reverse(first)
        second = self.reverse(second)
        carry = 0
        summ = 0
        
        temp = None     ## node to store reference of new element...
        curr = None
        res = None  ## to store refrence of final output after addition...
        
        while first != None or second != None:
            summ = carry + (first.data if first else 0 ) + ( second.data if second else 0)
            carry = (1 if summ>=10 else 0)
            summ = summ%10
            
            temp = Node(summ)
            if res == None:
                res = temp
            else:
                curr.next = temp
            curr = temp
            
            if first:
                first = first.next
            if second:
                second = second.next
        
        if carry>0:
            temp = Node(carry)
            curr.next = temp
            curr = temp
            
        res = self.reverse(res)
        return res

def printlist(head):
    res = []
    temp = head
    while(temp):
        res.append(f"{temp.data}")
        temp = temp.next
    return "-->".join(res)

## Driver code..!!!!

if __name__ == "__main__":
    first = Linkedlist()
    second = Linkedlist()
    first.insert(1)
    first.insert(9)
    first.insert(9)
    first.insert(9)
    
    second.insert(1)
    second.insert(2)
    
    print("list1-->>",first)
    print("list2-->>",second)
    
    final = Linkedlist()
    out = None
    out = final.addTwoLists(first.head, second.head)
    
    print("after adding final list-->",printlist(out))
    
    