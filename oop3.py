class Student:
    def __init__(self, name, age):
        # Initialize attributes
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Student: {self.name}, Age: {self.age}")

# 1. Collect the user input outside the class
user_name = input("Enter student name: ")
# Remember to cast numerical inputs to int or float
user_age = int(input("Enter student age: ")) 

# 2. Pass the variables to create the object
student1 = Student(user_name, user_age)
student1.display_info()