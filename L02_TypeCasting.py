# Typecasting = the process of converting a value from one data type to another
# int(), float(), str(), bool()

name = "Yanji"
age = 19
gpa = 6.7
is_student = True
age1 = 19

# making this a whole number by converting it to an integer
gpa = int(gpa)
print(gpa) 

# making the age a decimal number by converting it to a float
age = float(age)
print(age)


# making the integer a string by converting it to a string, it will get the variable of age and convert it to a string
age1 = str(age1)
# now it's a string not an integer
age1 = age1 + "1"
print(age1)
# now it' added the string "1" to the end of the string "191"

# if we run this boolean name, we will get True because the string "Yanji" is not empty
# if it was an empty string "" it would be False
name = bool(name)
print(name)

