#this program tests to see the strength of a password

import re

def passwordtester(x):
    upper = re.compile(r'[A-Z]')
    if upper.search(x) == None:
        return True
    lower = re.compile(r'[a-z]') 
    if lower.search(x) == None:
        return True
    digit = re.compile(r'[0-9]') 
    if digit.search(x) == None:
        return True
    length = re.compile(r'.{8,}') 
    if length.search(x) == None:
        return True
    else:
        return False

print("please enter your password")
password=input()

if passwordtester(password) == True:
   print ("this password frankly sucks")
elif passwordtester(password) == False:
   print ("congrats your password is secure")