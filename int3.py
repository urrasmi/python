class school:
    def get(self):
        print("get details")
class student(school):
    def show(self):
        print("student details") 
class parent(student):
    def display(self):
        print("parent details")

obj1=parent()
obj1.get()
obj1.show()
obj1.display()        
