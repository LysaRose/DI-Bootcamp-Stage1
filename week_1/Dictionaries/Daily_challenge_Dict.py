# Challenge 1
# Ask a user for a word
user_word = input("please choose a word: ")
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list and those lists are values.

letter_indexes = {}
for index, letter in enumerate(user_word):
    if letter not in letter_indexes:
        letter_indexes[letter] = []
    letter_indexes[letter].append(index)

print(letter_indexes)

# Challenge 2
# Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.
# Hint : make sure to convert the amount from dollars to numbers. Create a program that deletes the $ sign, and the comma (for thousands)

bookstore_items = {
    "Novel" : 50,
    "Mystery Book" : 98,
    "Science Fiction Book" : 85, 
    "Biography" : 105, 
    "Cookbook" : 125, 
    "Journal" : 25, 
    "Poetry Collection" : 47,
    "Travel Guide" : 130,
    "Children's Book" : 78,
    "Art Book" : 150
}

user_wallet = int(input("How much money do you have? "))
affordable_items = []

for item, price in bookstore_items.items():
     if user_wallet >= price:
        affordable_items.append(item)

affordable_items.sort()

if affordable_items:
    print("Items you can buy: ")
    for item in affordable_items:
        print(item)
else:
    print("Nothing")