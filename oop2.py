class School:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def show(self):
        print("Name= " +self.name )
        print("Age= " +self.age)
        
class Student(School):
    pass
class Teacher(School):
    pass
s1=Student("John",15)
t1=Teacher("Alice",50)
s1.show()
t1.show()