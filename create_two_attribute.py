#Create a "Person" class

#that has a name("name") and a age("age")
class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
a = Person('Shoxruh', 18)
b = Person('Nurbek', 19)
print(a.name, a.age, b.name, b.age)