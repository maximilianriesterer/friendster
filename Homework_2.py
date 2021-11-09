#task 1: The Greeting Program

name = "Maximilian"
from datetime import date
import calendar
curr_date = date.today()
print("Good day", name, ". Today,", calendar.day_name[curr_date.weekday()], "is a perfect day to learn some Python")


#task 2: Manipulate Strings
first_name = 'Maximilian'
last_name = 'Riesterer'
print("Hi there,", first_name + ' ' + last_name)


#task 3: Using Python as a calculator
a = 3
b = 4
aExp = pow(a, b)
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(aExp)