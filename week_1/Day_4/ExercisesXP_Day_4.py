# Exercise 1 : Favorite Numbers
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

my_fav_nums = [3, 5, 7, 9]
print(my_fav_nums)
my_fav_nums.append(11)
print(my_fav_nums)
my_fav_nums.remove(11)
print(my_fav_nums)
friend_nums = [2, 4, 6]
print(my_fav_nums)
our_fav_numbers = my_fav_nums + friend_nums
print(our_fav_numbers)

print("----------")

#Exercise 2: Tuple
#Given a tuple which value is integers, is it possible to add more integers to the tuple?

print("Q: Given a tuple which value is integers, is it possible to add more integers to the tuple?")
print("A: No, once a tuple is created it can not be changed")

print("----------")

# Exercise 3: List
# Instructions
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(basket)
basket.remove("Banana")
print(basket)
basket.remove("Blueberries")
print(basket)
basket.append("Kiwi")
print(basket)
basket.insert(0, "Apples")
print(basket)

appels_num = 0
for fruit in basket:
    if fruit == "Apples":
        appels_num += 1
        print("You have ", appels_num, "appels")

basket.clear()
print(basket)

print("----------")

# Exercise 4: Floats
# Instructions
# Recap – What is a float? What is the difference between an integer and a float?
# Create a list containing the following sequence of floats and integers (it should be a list with mixed types): 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
# Can you think of another way to generate a sequence of floats?

print("Q: What is the difference between an integer and a float?")
print("A: An integer is a full number like 3, 5, 7 and floats are divided numbers with a decimal point like 1.5, 2.4, 3.14")

list = 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5
print(list)

new_list = []

for i in range(1,6): 
    new_list.append(i + 0.5)
    new_list.append(i)
print(new_list)

print("----------")

# Exercise 5: For Loop
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

nums_list = []
for i in range(1,21):
    print(i)

for i in range(1,21):
    if i % 2 == 0 :
        print(i)

print("----------")

# Exercise 6 : While Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
name = ""
while name != "lysa":
    name = input("What is your name?")

print("Welcome!")

print("----------")

#  Exercise 7: Favorite fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

fav_fruit = input("What are your favorit fruits? (please, separate the fruits with a single space) ")
fruits = fav_fruit.split()
for fruit in fruits:
  print(fruit)

new_fruit = input("Choose any fruit: ")
if new_fruit in fruits :
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")

print("----------")

# Exercise 8: Who ordered a pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

toppings = []
while True:
    topping = input("Choose a topping for your pizza?(or 'quit' to stop):")
    toppings.append(topping)
    
    if topping == "quit" :
        break 
        
    else: 
        print("I’ll add that topping to your pizza. Choose another one?(or 'quit' to stop):")
    
        base_price = 10
        topping_price = 2.5
        total_price = base_price + (int(len(toppings)) * topping_price)
        
print("your total pize is " + str(total_price) + (" NIS, 10 NIS for the base and 2.5 NIS per topping") )

print("----------")

# Exercise 9: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

##A 
# Ask a family the age of each person who wants a ticket.
# Store the total cost of all the family’s tickets and print it out.


print("A")
total_cost = 0

while True :
    age = input("how old are you?")

    if age == "quit" :
        break

    elif int(age) <= 3 :
        print("how old is the next person in your family? or quit")
    elif 3 <= int(age) <= 12 :
        print("how old is the next person in your family? or quit")
        total_cost += 10
    elif int(age) > 12 :
        print("how old is the next person in your family? or quit")
        total_cost += 15

        # bayby_price = 0
        # child_price = 10
        # adult_price = 15

print("Your total is of " + str(total_cost) + " NIS")

##B
# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between
# the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age,
#  if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.

print("B")


teens_names = ["Danny", "Yoav", "Noa", "Dana"]

for teen in teens_names[:]:
    age = input("how old is " + teen + "?" )

    age = int(age)
    
    if 21 >= age <= 16 :
        teens_names.remove(teen)

print(str(teens_names) + "can watch the movie")

print("----------")

# Exercise 10 : Sandwich Orders
# Instructions
# Using the list below :

# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]


sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders.

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
    print(sandwich_orders)

# We need to prepare the orders of the clients:
# Create an empty list called finished_sandwiches.

finished_sandwiches = []

# One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.

while sandwich_orders :
    sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(sandwich)

# After all the sandwiches have been made, print a message listing each sandwich that was made, such as:
# I made your tuna sandwich
# I made your avocado sandwich
# I made your egg sandwich
# I made your chicken sandwich

    print("I made your " + sandwich)