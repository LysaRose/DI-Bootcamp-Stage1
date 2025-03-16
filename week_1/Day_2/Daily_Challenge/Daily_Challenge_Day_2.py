# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.
# If it’s 10 characters, print a message which states “perfect string” and continue the exercise.

string = input("Enter a string: ")

if len(string) < 10 :
    print("string not long enough")
elif len(string) > 10 :
    print("string too long")
elif len(string) == 10 :
    print("perfect string")

print("----------")

print(string[0])
print(string[-1])

print("----------")

for i in range(1, len(string) + 1):
    print(string[:i])