# logical operators = evaluate multiple conditions (or, and, not)
#       or = at least one conditon must be True
#       and = both conditon must be True
#       not = inverts the condition (not False, not True)

# Or Example

# Temperature

temp = float(input("What is the temperature? "))
is_raining = False # False = not raining, True = Raining

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")

# Battery

battery = int(input("What is your phone battery %? "))
charger = input("Is your charger plugged in? Yes or No: ")

has_charger = charger == "Yes"

if battery > 20 or has_charger:
    print("You can play games")
else:
    print("Phone will die. Cannot play games")

    # And Example

# Temperature

temp = int(input("What is the temperature? "))
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT outside")
    print("It is Sunny")
elif temp <= 0 and is_sunny:
    print("It is COLD outside")
    print("It is Sunny")
elif temp < 28 and temp > 0 and is_sunny:
    print("It is WARM outside")
    print("It is Sunny")

    # Cinema Ticket

    age = int(input("How old are you? "))
    ticket = input("Do you have a ticket? Yes/No:")
    has_ticket = ticket == "Yes"
    
    if age >= 18 and has_ticket:
        print("Welcome to the cinema! Enjoy the movie :)")
    else:
        print("Sorry, You cannot enter :(")

# Not Example
        # Log In 

logged_in = input("Are you logged in? Yes/No: ")
is_logged_in = logged_in == "Yes" # turns Yes/No into True/False
        
if not is_logged_in: # not True = False, not False = True

        # This runs only if is_logged_in is False
        # Because not False = True
    print("Please log in first!")
else:
    print("Welcome back!") # Because not True = False, so we skip the if 
