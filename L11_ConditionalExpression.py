# Conditional Expression = A one line shortcut for the if else statement (ternary operator)
# print or assign one of two values based on condition
# X if condition else Y

# Positive or Negative
num1 = int(input("Enter a number: "))
print("Positive" if num1 > 0 else "Negative")

# Even or odd
num2 = int(input("Enter a number: "))
result = "EVEN" if num2 % 2 == 0 else "ODD"
print(result)

# Max Number

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
max_num = a if a > b else b

print(f"The max number is {max_num}")

# Minimum Number

c = int(input("Enter first number: "))
d = int(input("Enter second number: "))
min_num = c if c < d else d
print(f"The minimum number is {min_num}")

# Age

age = int(input("Enter your age: "))
status = "Adult" if age >= 18 else "Minor"
print(f"You are {status}")

# Access Level

user_role = input("What is your access? ")
access_level = "Full Access" if user_role == "Admin" else "Limited Access"
print(access_level)