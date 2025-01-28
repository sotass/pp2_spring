#1
# Create a class named MyClass:

class MyClass:
  x = 5

#2
class MyClass:
  x = 5

p1 = MyClass()

#3
# Use the p1 object to print the value of x:

class MyClass:
  x = 5

p1 = MyClass()

print(p1.x)

#4  
# What is the correct syntax to assign a "init" function to a class?

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

#5
class Person:
   def __init__(self, name, age):
    self.name = name
    self.age = age
   def __str__ (self):
    return f'{self.name}({self.age})
p1 = Person('John', 36)
print(p1)