# if = do some code only IF some condititon is True
# Else do something else

# Age Example

age = int(input("Enter your age:"))

if age >= 100: # True do something
    print("You are too old to sign up")

elif age >= 18:   # True If
    print("You are now signed up!")

elif age < 0:   # Else If
    print("You haven't been born yet")
elif age >= 100:
    print("You are too old to sign up")

else:   # False Else
    print("You must be 18+ to sign up!")

# Food Example

response = input("Would you like food? (Y/N): ")

if response == "Y":  # For comparison use 2 equals
    print("Have some food!")
else:
    print("No food for you")


    # Name Example

    name = input("Enter your name:")

    if name == "":
        print("You did not type in your name!")
    else:
        print(f"Hello, {name}")

        # Booleans with If Statments

        for_sale = True

        if for_sale:
            print("This item is for sale")
        else:
            print("This item is not for sale")