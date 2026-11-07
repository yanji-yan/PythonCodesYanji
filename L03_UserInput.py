# input() a function that prompts the user to enter data
# Returns the entered data as a string
# use f string if you want to insert variables

name = input("What is your name? ")
age = int(input("What is your age? "))

age += 1

print(f"Hello, {name}!")
print("HAPPY BIRTHDAY!")
print(f"You are {age} years old.")
