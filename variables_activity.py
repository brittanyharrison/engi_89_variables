"""
Activity/task
variables first_name, last_name, age, DOB
prompt user to input above value
print/display the type of each value received from the user
then display the data back to user with greeting message
"""
# Request for user to input their first name
first_name = input("What is your first name?")
# Displays the value type of the first_name variable
print(type(first_name))


# Request for user to input their last name
last_name = input("What is your last name?")
# Displays the value type of the last_name variable
print(type(last_name))


# Request for user to input their last age
age = int(input("How old are you?"))
# Displays the value type of the age variable
print(type(age))


# Request for user to input their date of birth
DOB = input("What is your date of birth?(DD/MM/YYYY) ")
# Displays the value type of the age variable
print(type(DOB))

Greeting = "Hi " + first_name + last_name + "! You were born on " + DOB + ", so you are " + str(age) + " years old."
print(Greeting)
