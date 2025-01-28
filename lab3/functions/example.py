#1
def my_function():
  print("Hello from a function")

#2
def my_function():
  print("Hello from a function")

my_function()

#3
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#4
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#5
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil") #its not correct

#6
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#7
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#8
# If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#9
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#10
# To let a function return a value, use the return statement:
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#11
def myfunction():
  pass

# having an empty function definition like this, would raise an error without the pass statement


#12
# To specify that a function can have only positional arguments, add , / after the arguments:
def my_function(x, /):
  print(x)

my_function(3)

#13
# Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:
def my_function(x):
  print(x)

my_function(x = 3)

#14
# But when adding the , / you will get an error if you try to send a keyword argument:
def my_function(x, /):
  print(x)

my_function(x = 3) #thats not correct

#15
# To specify that a function can have only keyword arguments, add *, before the arguments:
def my_function(*, x):
  print(x)

my_function(x = 3)

#16
# Without the *, you are allowed to use positionale arguments even if the function expects keyword arguments:
def my_function(x):
  print(x)

my_function(3)

#17
# But with the *, you will get an error if you try to send a positional argument:
def my_function(*, x):
  print(x)

my_function(3) #error

#18
# Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

#19
# Recursion Example
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)

