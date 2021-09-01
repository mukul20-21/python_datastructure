class student:
    clg = "Samrat ashok"
    year = "3rd year m aa gaye ho mehnet karo"
    
    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name
        
    def display(self):
        print("roll number of student in clg:", self.rollno)
        print("Name of student:", self.name)
        print("used class variable here:", student.clg)
        print(student.year)

rollno = int(input("Enter the roll no of student"))
name = input().strip()

student1 = student(rollno,name)
student1.display()