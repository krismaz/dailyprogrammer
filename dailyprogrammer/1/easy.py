#Quick and dirty

name = input("Name?")
age = input("Age?")
username = input("Username?")

print('Your name is {}, you are {} years old, and your username is {}'.format(name, age, username))

with open('last', 'w') as file:
	file.write(','.join([name, age, username]))