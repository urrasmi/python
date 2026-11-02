class Student:
      def __init__(self,name,age,mark):
            self.name=name
            self.age=age
            self.mark=mark
            
      def show(self):
            print("name of the student  " + self.name)
            
s1=Student("Anu",23,45)
s2=Student("Minu",24,47)
s1.show()       