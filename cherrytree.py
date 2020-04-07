import random

print('''
Café CherryTree - Password Generator
_________________________________

''')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

number = input('How many we cooking for? ')
number = int(number)

length = input('How many courses? ')
length = int(length)

print('\nBon Appetit!')

for pwd in range(number):
  password = ''
  for c in range(length):
    password += random.choice(chars)
  print(password)