class Animal:
    def speak(self):
        print("Animal sound")
        
class Bird(Animal):
    def fly(self):
        print("flying bird")
        
class Dog(Bird): 
    def sound(self):
        print("Bow Bow....") 
        

d1=Dog()
print(d1.speak())
print(d1.sound())
print(d1.fly())