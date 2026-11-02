class Animal:
    def speak(self):
        print("Animal sound")
        
class Dog(Animal): 
    def sound(self):
        print("Bow Bow....") 
        

d1=Dog()
print(d1.speak())
print(d1.sound())