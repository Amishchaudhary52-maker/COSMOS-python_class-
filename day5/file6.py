class Student:
    def __init__(self,name):
        self.name=name
    def greet(self):
        return f"Hi,I'm {self.name}"
    
s1=Student("Amish")
print(s1.greet())