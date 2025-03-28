#  Exercise 1 : Convert lists into dictionaries
# Instructions
# Convert the two following lists, into dictionaries.
# Hint: Use the zip method
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ["Ten", "Twenty", "Thirty"]
values = [10, 20, 30]

new_list = dict(zip(keys, values))

print(new_list)

print("----------")

#  Exercise 2 : Cinemax #2#  Exercise 2 : Cinemax #2
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Given the following object:

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


# How much does each family member have to pay ?

# Print out the family’s total cost for the movies.

cost = 0

family = {
    "rick": 43, 
    'beth': 13, 
    'morty': 5, 
    'summer': 8
    }
for name, age in family.items():
    if int(age) < 3:
        continue
    elif 3 <= int(age) <= 12 :
        cost += 10
    elif int(age) > 12:
        cost += 15
print("Your total is of " + str(cost) + " NIS")

print("----------")

#  Exercise 3: Zara
# Instructions
# Here is some information about a brand.
# name: Zara 
# creation_date: 1975 
# creator_name: Amancio Ortega Gaona 
# type_of_clothes: men, women, children, home 
# international_competitors: Gap, H&M, Benetton 
# number_stores: 7000 
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green


# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
# The values type_of_clothes and international_competitors should be a list. The value of major_color should be a dictionary.
brand = {
        "name" : "Zara", 
        "creation_date" : 1975,  
        "creator_name" : "Amancio Ortega Gaona ", 
        "type_of_clothes": "men, women, children and home",  
        "international_competitors" : "Gap, H&M, Benetton", 
        "number_stores" : 7000, 
        "major_color": {
            "France" : "blue", 
            "Spain" : "red", 
            "US" : "pink, green",
        }
}
# 3. Change the number of stores to 2.
brand["number_stores"] = 2
print(brand["number_stores"])
# 4. Use the key [type_of_clothes] to print a sentence that explains who Zaras clients are.
print("In our brand we sell cloth for ", brand["type_of_clothes"], " .")
# 5. Add a key called country_creation with a value of Spain.
brand.update({"country_creation" : "Spain"})
print(brand)
# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
print(brand.get("international_competitors"))
brand["international_competitors"] += ", Desigual"
print(brand["international_competitors"])
# 7. Delete the information about the date of creation.
del(brand["creation_date"])
print(brand)
# 8. Print the last international competitor.
competitors_list = brand["international_competitors"].split(", ")
print(competitors_list[-1])
# 9. Print the major clothes colors in the US.
print(brand["major_color"])
# 10. Print the amount of key value pairs (ie. length of the dictionary).
amount_of_keys = len(brand.keys())
print(amount_of_keys)
# 11. Print the keys of the dictionary.
print(brand.keys())
# 12. Create another dictionary called more_on_zara with the following details:

# creation_date: 1975 
# number_stores: 10 000
more_on_zara = {
    "creation_date" : 1975,
    "number_stores" : 10000
}
# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
brand.update(more_on_zara)
print(brand)
# 14. Print the value of the key number_stores. What just happened ?
print(brand["number_stores"])
print("Q: what just happened? \nA: it changed" )

print("----------")

# Exercise 4 : Disney characters
# Instructions
# Use this list :

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
# Analyse these results :
# #1/
# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
disney_user_A = {user : index for index, user in enumerate(users)}
print(disney_user_A)
# #2/
# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
disney_user_B = {index : user for index, user in enumerate(users)}
print(disney_user_B)
# #3/ 
# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
sorted_users = sorted(users)
disney_user_C = {user : index for index, user in enumerate(sorted_users)}
print(disney_user_C)
# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
disney_user_A = {}

for index , user in enumerate(users):
    disney_user_A[user] = index

print(disney_user_A)
# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
disney_user_B = {}

for index , user in enumerate(users):
    disney_user_B[index] = user

print(disney_user_B)
# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
sorted_users = sorted(users)

disney_user_C = {}

for index , user in enumerate(sorted_users):
    disney_user_C[user] = index

print(disney_user_C)
# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
disney_users_with_i = {user: index for index, user in enumerate(users) if "i" in user}

print(disney_users_with_i)
# The characters, which names start with the letter “m” or “p”.
disney_users_with_m_p = {user: index for index, user in enumerate(users) if user[0].lower() in ["m", "p"]}

print(disney_users_with_m_p)

print("----------")
