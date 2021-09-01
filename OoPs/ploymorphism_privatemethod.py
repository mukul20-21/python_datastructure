class car:
    def __init__(self):
       print("As object declare it first goes to init method inside the class")
       #self.__updatesoftware()         # private method calling using intance(object) variable self
    def drive(self):
        print("driving method of class call outside by object of class car...!!!")
    
    def __updatesoftware(self):
        print("Update software...!!! \n calling by instance variable using class contructor __init__")

blackcar = car()                    # automatic calls the init method declare in class
blackcar.drive()
blackcar.__updatesoftware()         # AttributeError:calling outside the class private method it cause error...!!!
