from datetime import datetime
name = input('What is your name? \n')
age = int(input('How old are you? \n'))
next_birthday = int(age+1)
print ('Hello %s. You are %s years old. On your next birthday you will be %s years old.' % (name, age, next_birthday))