class car:
    __maxspeed = 0          # initialize the private variable with double underscore
    __name = " "
    
    def __init__(self):
        self.__maxspeed = 200       # initialize instance variable for manipulation in private variable
        print("Evoke constructor as object of class car is define...!!! \n")
        self.__name = "Mukul print with the help of instance variable"
        
    def drive(self):
        print("driving the car....!!! \t calling method of call and it is public function")
        print(self.__maxspeed)
        print(self.__name)
     
    def setspeed(self,speed):  # here the speed variable initialize outside the class
        self.__maxspeed = speed
        print(self.__maxspeed)

redcar = car()
redcar.drive()
redcar.setspeed(1000)