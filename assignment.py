

class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    
    def Introduce(self):
        print(f'Hello! My name is {self.name}, I am a {self.age} year old {self.gender}.')

obj=Person('Daniel',20,'Male')

obj.Introduce()