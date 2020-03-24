"""
Write a regular expression that can detect dates in the DD/MM/YYYY format.
Assume that the days range from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999.
Note that if the day or month is a single digit, it’ll have a leading zero.

The regular expression doesn’t have to detect correct days for each month or for leap years; 
it will accept nonexistent dates like 31/02/2020 or 31/04/2021. Then store these strings into variables 
named month, day, and year, and write additional code that can detect if it is a valid date. April, June, 
September, and November have 30 days, February has 28 days, and the rest of the months have 31 days. February
has 29 days in leap years. Leap years are every year evenly divisible by 4, except for years evenly divisible 
by 100, unless the year is also evenly divisible by 400. Note how this calculation makes it impossible to make
a reasonably sized regular expression that can detect a valid date.
"""

import re

def isvaliddate(x): #DD/MM/YYYY
    date_regex = re.compile(r'(\d{2})/(\d{2})/(\d{4})')
    date = date_regex.search(x)
    
    day = date.group(1) #01-31
    month = date.group(2) #01-12
    year = date.group(3) #1000-2999
    excpt = ['02','04','06','09','11'] # February, April, June, September, and November exceptions

    if int(day) < 1 or int(day) > 31:
        return False
    elif int(month) < 1 or int(month) > 12:
        return False
    elif int(year) < 1000 or int(year) > 2999:
        return False
    elif int(day) == 31 and month in excpt:
        return False
    elif int(month) == 2 and int(day) == 30:
        return False
    elif int(month) == 2 and int(day) == 29:
        if (int(year) % 4) == 0:
            if (int(year) % 400) == 0:
                return True
            elif (int(year) % 100) == 0:
                return False
            else:
                return True
        else:
            return False
    else:
        return True

# Tests:
print (isvaliddate('00/01/2000')) #False
print (isvaliddate('01/00/2000')) #False
print (isvaliddate('01/01/0000')) #False
print (isvaliddate('31/04/2000')) #False
print (isvaliddate('30/02/2000')) #False
print (isvaliddate('29/02/2000')) #True  divisible by 400
print (isvaliddate('29/02/2100')) #False divisible by 100
print (isvaliddate('29/02/2004')) #True  divisible by 4
print (isvaliddate('29/02/2003')) #False non-divisible by 4
print (isvaliddate('28/02/2003')) #True