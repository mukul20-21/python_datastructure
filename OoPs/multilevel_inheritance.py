#base class
class person:
    def dislay(self):
        print("Here the element of base class person...!!!! \n")

#derived class_1    
class employee(person):
    def printing(self):
        print("Here the element of first element of derived class.....!!!! \n")

# derived class_2
class programmer(employee):
    def show(self):
        print("Here the 2nd derived class from first derived class employee")

p1 = programmer()
p1.dislay()
p1.printing()
p1.show()