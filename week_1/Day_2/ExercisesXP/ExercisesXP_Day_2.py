# Print the following output in one line of code:

# Hello world
# Hello world
# Hello world
# Hello world

print("Hello world \nHello world \nHello world \nHello world")

print("----------")

# Write code that calculates the result of: (99^3)*8 (meaning 99 to the power of 3, times 8).

print((99 ** 3) * 8)

print("----------")

# Predict the output of the following code snippets:

# >>> 5 < 3
# >>> 3 == 3
# >>> 3 == "3"
# >>> "3" > 3
# >>> "Hello" == "hello"

False
True
False
False
False

print("----------")

# Create a variable called computer_brand which value is the brand name of your computer.
# Using the computer_brand variable print a sentence that states the following: "I have a <computer_brand> computer".

computer_brand = "LylooComp"
print("I have a " + computer_brand + " computer")

print("----------")

# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3.
# Have your code print the info message.
# Run your code

name = "Lysa" 
age = 26
shoe_size = 40
info = f"I am {name}, I am {age}, my shoe size is {shoe_size}, and I have a degree in animation" 

print (info)

print("----------")

# Create two variables, a and b.
# Each variable value should be a number.
# If a is bigger then b, have your code print Hello World.

a = 5
b = 3
if a > b:
    print("Hello world")

print("----------")  

# Write code that asks the user for a number and determines whether this number is odd or even.

number= int(input("Choose a number: "))

if number % 2 == 0 :
    print("The number is even")
else:
    print("The number is odd")
    
print("----------")  

# Write code that asks the user for their name and determines whether or not you have the same name, 
# print out a funny message based on the outcome.

my_name = "lysa"
name = input("What is your name?")

if name == my_name:
    print("Welcome to our cult")
else:
    print("I'm sorry but you can not be part of our cult!")

print("----------")  

# Write code that will ask the user for their height in centimeters.
# If they are over 145cm print a message that states they are tall enough to ride.
# If they are not tall enough print a message that says they need to grow some more to ride.

height = int(input("What is your height in centimeters? "))

if height > 145 :
    print("You are tall enough to ride")
else:
    print("You need to grow some more to ride")