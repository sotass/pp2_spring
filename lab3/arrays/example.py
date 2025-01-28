# An array is a special variable, which can hold more than one value at a time.

#1
# Create an array containing car names:

cars = ["Ford", "Volvo", "BMW"]

#2
# Get the value of the first array item:

x = cars[0]

#3
# Modify the value of the first array item:

cars[0] = "Toyota"

#4
# Return the number of elements in the cars array:

x = len(cars)

#5
# Print each item in the cars array:

for x in cars:
  print(x)

#6
# Add one more element to the cars array:

cars.append("Honda")

#7
# Delete the second element of the cars array:

cars.pop(1)

#8
# Delete the element that has the value "Volvo":

cars.remove("Volvo")