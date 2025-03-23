# 🌟 Exercise 1 : What are you learning ?
# Instructions
# Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
def display_message() :
    print("In this class we are learning about Python!")
# Call the function, and make sure the message displays correctly.
display_message()

print("----------")

#  Exercise 2: What’s your favorite book ?
# Instructions
# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as "One of my favorite books is <title>".
# For example: “One of my favorite books is Alice in Wonderland”
def favorit_book(title):
     print(f"One of my favorite books is {title}.")
# Call the function, make sure to include a book title as an argument when calling the function.
favorit_book("Harry Potter")

print("----------")

# 🌟 Exercise 3 : Some Geography
# Instructions
# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as "<city> is in <country>".
# For example “Reykjavik is in Iceland”
# Give the country parameter a default value.
# Call your function.
def describe_city(city, country="Israel"):
    print(f"{city} is in {country}")

describe_city("Ashdod", "Israel")
describe_city("Ashsod")


print("----------")

# Exercise 4 : Random
# Instructions
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
#  Use the random module.
# Compare the two numbers, if it’s the same number, display a success message, 
# otherwise show a fail message and display both numbers.

import random

def comparing(user_num) :
    random_num = random.randint(1, 100)
    if user_num == random_num:
        print("Success!!")
    else:
        print(f"Fail!! your number {user_num} is not equal to random number {random_num}")

user_num = int(input("Choose a number from 1 to 100:" ))

comparing(user_num)

print("----------")

# 🌟 Exercise 5 : Let’s create some personalized shirts !
# Instructions
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# Call the function make_shirt().
# Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# Call the function, in order to make a large shirt with the default message
# Make medium shirt with the default message
# Make a shirt of any size with a different message.

def make_shirt(size = "L", message = "I love Python"):
    print(f"The size of the shirt is {size} and the text is {message}")
make_shirt()
make_shirt("M", )
make_shirt("XXL", "Happy B-Day")

print("----------")

#🌟 Exercise 6 : Magicians …
# Instructions
# Using this list of magician’s names

# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# Create a function called show_magicians(), which prints the name of each magician in the list.
def show_magicians(names):
    for name in names:
        print(name)
show_magicians(magician_names)
# Write a function called make_great() 
# that modifies the original list of magicians by adding the phrase "the Great" to each magician’s name.
def make_great(names):
     return [name + " the Great" for name in names]

magician_names = make_great(magician_names)
print(magician_names)
# Call the function make_great().
make_great(magician_names)
# Call the function show_magicians() to see that the list has actually been modified.
show_magicians(magician_names)

print("----------")


# 🌟 Exercise 7 : Temperature Advice
# Instructions
# Create a function called get_random_temp().
import random
def get_random_temp():
# This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
    random_num = random.randint(-10, 40)
    return random_num
# Test your function to make sure it generates expected results.
temp = get_random_temp()
print(temp)
# Create a function called main().
# Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”
# Let’s add more functionality to the main() function. 
# Write some friendly advice relating to the temperature: 
# below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# between 16 and 23
# between 24 and 32
# between 32 and 40
def main():
    temp = get_random_temp()
    print(f"The temperature right now is {temp} degrees celsius.")

    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif 0 < temp < 16 :
        print("Quite chilly! Don’t forget your coat")
    elif 16 < temp <23 :
        print("It's a bit cool outside, but not too bad.")
    elif 24 < temp < 32 :
        print("The weather is warm, perfect for outdoor activities!")
    else:
        print("It's really hot outside! Stay cool and hydrated")

main()

# Change the get_random_temp() function:
# Use the season as an argument when calling get_random_temp().
# Add a parameter to the function, named ‘season’. 
# Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
import random
def get_random_temp(season):
    if season == "winter":
        random_num = random.randint(-10, 10)
    elif season == "spring":
        random_num = random.randint(11, 20)
    elif season == "summer":
        random_num = random.randint(21, 40)
    elif season == "autumn":
        random_num = random.randint(0, 16)
  
    return random_num

# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. 
# Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
def main() :
    season = input("Enter the season (winter, spring, summer, autumn): ")
    temp = get_random_temp(season)
    if temp is not None:
        print(f"The random temperature in {season} is: {temp}°C")

main()

print("----------")

# 🌟 Exercise 8 : Star Wars Quiz
# Instructions
# This project allows users to take a quiz to test their Star Wars knowledge.
# The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.

# Here is an array of dictionaries, containing those questions and answers

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]


# Create a function that asks the questions to the user, and check his answers.
            
#  Track the number of correct, incorrect answers. Create a list of wrong_answers
# Create a function that informs the user of his number of correct/incorrect answers.


def ask_questions():

    correct = 0
    wrong = 0
    wrong_list = []

    for q in data:
        user_answer = input(q["question"]).strip()
        if user_answer == q["answer"]:
             correct += 1
             
        else:
            wrong += 1
            wrong_list.append(f"The answer to  '{q['question']}' was {q['answer']}")
           

    return correct, wrong, wrong_list



def display_results(correct, wrong, wrong_list):
    print(f"You got {correct} correct answers!")
    print(f"You got {wrong} incorrect answers!")
    
    if wrong > 0:
        print("The questions you answered wrong:")
        for wrong_answer in wrong_list:
            print(wrong_answer)
def main():
    correct, wrong, wrong_list = ask_questions()  
    display_results(correct, wrong, wrong_list)

main()