# @ferus-wylde

# Import libraries

import sys
import random
from termcolor import cprint
from pyfiglet import figlet_format


# Password Generator for non-InfoSec use

print('\n')

# ASCII title

cprint(figlet_format('CherryTree', font='standard'), 'red', attrs=['bold', 'dark'])

# Exhaustive list of pronounceable words in Adjective+Noun+Num+Punctuation format

chars = ['Aggressive', 'Alert', 'Alive', 'Ancient', 'Anxious', 'Arrow', 'Attractive', 'Average', 'Bad', 'Beautiful', 'Beige', 'Better', 'Big', 'Bitter', 'Black', 'Blue', 'Brown', 'Bumpy', 'Busy', 'Careful', 'Cheap', 'Chestnut', 'Clear', 'Cold', 'Combative', 'Cool', 'Cotton','Crazy', 'Crooked', 'Crystal', 'Dangerous', 'Dead', 'Delicious', 'Dim', 'Drab', 'Dry', 'Dull', 'Dusty', 'Elderly','Excited', 'Expensive', 'Fancy', 'Fat', 'Few', 'Filthy', 'Fresh', 'Fuzzy', 'Giant', 'Good', 'Graceful', 'Granite', 'Green', 'Handsome', 'Happy', 'Hard', 'Harsh', 'Hollow', 'Hot', 'Huge', 'Hungry', 'Large', 'Lazy', 'Light', 'Long', 'Low', 'Massive', 'Mellow', 'Melodic', 'Miniscule', 'Modern', 'New', 'Noisy', 'Oak', 'Octagonal', 'Old', 'Orange', 'Oval', 'Petite', 'Pink', 'Plain', 'Plastic', 'Poor', 'Puny', 'Purple', 'Quiet', 'Rainy', 'Red', 'Rich', 'Right', 'Round', 'Sad', 'Safe', 'Salty', 'Sane', 'Scared', 'Shallow', 'Sharp', 'Shiny', 'Short', 'Shrill', 'Shy', 'Skinny', 'Small', 'Soft', 'Solid', 'Sore', 'Sour', 'Square', 'Steep', 'Sticky', 'Strong', 'Superior', 'Sweet', 'Swift', 'Tan', 'Tart', 'Teak', 'Teeny', 'Terrible', 'Tiny', 'Tired', 'Tremendous', 'Triangular', 'Ugly', 'Unusual', 'Weak', 'Weary', 'Wet', 'Whispering', 'White', 'Wild', 'Wooden', 'Woolen', 'Wrong', 'Young', 'Red', 'Blue', 'Green', 'Purple', 'Yellow', 'Black', 'White', 'Pink', 'Silver', 'Gold', 'Indigo', 'Cherry']

chars_2 = ['Arm', 'Army', 'Baby', 'Bag', 'Ball', 'Band', 'Basin', 'Basket', 'Bath', 'Bed', 'Bee', 'Bell', 'Berry', 'Bird', 'Blade', 'Board', 'Boat', 'Bone', 'Book', 'Boot', 'Bottle', 'Box', 'Boy', 'Brain', 'Brake', 'Branch', 'Brick', 'Bridge', 'Brush', 'Bucket', 'Bulb', 'Button', 'Cake', 'Camera', 'Card', 'Cart', 'Carriage', 'Cat', 'Chain', 'Cheese', 'Chest', 'Chin', 'Church', 'Circle', 'Clock', 'Cloud', 'Coat', 'Collar', 'Comb', 'Cord', 'Cow', 'Cup', 'Curtain', 'Cushion', 'Dog', 'Door', 'Drain', 'Drawer', 'Dress', 'Drop', 'Ear', 'Egg', 'Engine', 'Eye', 'Face', 'Farm', 'Feather', 'Finger', 'Fish', 'Flag', 'Floor', 'Fly', 'Foot', 'Fork', 'Fowl', 'Frame', 'Garden', 'Girl', 'Glove', 'Goat', 'Gun', 'Hair', 'Hammer', 'Hand', 'Hat', 'Head', 'Heart', 'Hook', 'Horn', 'Horse', 'Hospital', 'House', 'Island', 'Jewel', 'Kettle', 'Key', 'Knee', 'Knife', 'Knot', 'Leaf', 'Leg', 'Library', 'Line', 'Lip', 'Lock', 'Map', 'Match', 'Monkey', 'Moon', 'Mouth', 'Muscle', 'Nail', 'Neck', 'Needle', 'Nerve', 'Net', 'Nose', 'Nut', 'Office', 'Orange', 'Oven', 'Parcel', 'Pen', 'Pencil', 'Picture', 'Pig', 'Pin', 'Pipe', 'Plane', 'Plate', 'Plough', 'Pocket', 'Pot', 'Potato', 'Prison', 'Pump', 'Rail', 'Rat', 'Receipt', 'Ring', 'Rod', 'Roof', 'Root', 'Sail', 'School', 'Scissors', 'Screw', 'Seed', 'Sheep', 'Shelf', 'Ship', 'Shirt', 'Shoe', 'Skin', 'Skirt', 'Snake', 'Sock', 'Spade', 'Sponge', 'Spoon', 'Spring', 'Square', 'Stamp', 'Star', 'Station', 'Stem', 'Stick', 'Stocking', 'Stomach', 'Store', 'Street', 'Sun', 'Table', 'Tail', 'Thread', 'Throat', 'Thumb', 'Ticket', 'Toe', 'Tongue', 'Tooth', 'Town', 'Train', 'Tray', 'Tree', 'Trousers', 'Umbrella', 'Wall', 'Watch', 'Wheel', 'Whip', 'Whistle', 'Window', 'Wing', 'Wire', 'Worm', 'Table', 'Door', 'Cat', 'Dog', 'Camel', 'Sheep', 'Duck', 'Badger', 'Fox', 'Shark', 'Fish', 'Tiger', 'Shark', 'Hawk', 'Rat', 'Chicken', 'Apple', 'Tree']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

numbers_2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

punct = ['!', "?", "#", "$", "£"]

number = input('''Cherries needed?
''')
number = int(number)

print('\n')

# Create output file to write in current directory

f = open('passwords.txt','w')

# Lottery pick from wordsheet 
def run():
  for pwd in range(number):
    password = ''
    password += random.choice(chars)
    password += random.choice(chars_2)
    password += random.choice(numbers)
    password += random.choice(numbers_2)
    password += random.choice(punct)
    print(password)

    f.write(password + '\n')

  ask = str(input('\nStill hungry?\n'))
  if ask.lower() in ('yes','y', 'Yes', 'ye', 'YES', 'yep'):
      print('\n')  
      run()
  else:
      print('')

f.close

run()
print('Bon Appetit!\n')
