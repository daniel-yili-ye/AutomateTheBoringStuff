"""
Write a program that asks users for their sandwich preferences. The program should use PyInputPlus to ensure that they 
enter valid input, such as:

Using inputMenu() for a bread type: wheat, white, or sourdough.
Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
Using inputYesNo() to ask if they want cheese.
If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.
Come up with prices for each of these options, and have your program display a total cost after the user enters their selection.
"""

import pyinputplus as pyip

menu = {'wheat':1.25,'white':1,'sourdough':2,'chicken':3,'turkey':3.25,'ham':2.5,'tofu':3,'cheddar':1,'swiss':1,'mozzarella':1.25,'sauce':0.5}

total_price = 0
bread = pyip.inputMenu(['wheat','white','sourdough'],prompt='Bread type: ')
protein = pyip.inputMenu(['chicken','turkey','ham','tofu'],prompt='Protein type: ')
total_price = (menu[bread] + menu[protein])
cheese = pyip.inputYesNo('Cheese?: ')
if cheese == 'yes':
    cheese_type = pyip.inputMenu(['cheddar','swiss','mozzarella'],prompt='Cheese type: ')
    total_price += menu[cheese_type]
sauce = pyip.inputYesNo('Sauce?: ')
if sauce == 'yes':
    total_price += menu['sauce']
sandwich_count = pyip.inputInt('Number of Sandwiches: ',min=1)
total_price *= sandwich_count

print (total_price)
