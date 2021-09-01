## Create the hashing function which insert a key into tables...!!!!

class myhash:
    def  __init__ (self, b):                ## b = size of m declare while create the object of class...
        self.bucket = b
        self.table = [[] for i in range(b)]

    def  insert (self, x):                  ## x = key values which insert into hash table....!!!!!
        i = x % self.bucket                 ## hash function declaration...!!!
        self.table[i].append(x)          
    
    def  delete (self, x):
        i = x % self.bucket
        if  x in self.table[i]:
            self.table[i].remove(x)
    
    def  search (self, x):
        i = x % self.bucket
        return x in self.table[i]

### Drivers code....

h = myhash(7)
h.insert(70)
h.insert(71)
h.insert(9)
h.insert(56)
h.insert(72)

print ("search for a element...---",h.search(56))

h.delete(56)

print(h.search(56))
    