#this program is a regex version of strip

import re

def regexstrip(x,y):
    
    #to remove outermost white spaces around the string first
    leftstrip = re.compile(r'^\s*')
    tempvar = leftstrip.sub('',x)
    rightstrip = re.compile(r'\s*$')
    answer_1 = rightstrip.sub('',tempvar)

    #to remove specified input and ignore case
    removestrip = re.compile(y,re.I)
    tempvar = removestrip.sub('',answer_1)
    return (tempvar)

print ("please enter the string that you would like to strip")
strip_1 = input()
print ("what characters would you like to remove from this string?")
strip_2 = input()
print (regexstrip(strip_1,strip_2))