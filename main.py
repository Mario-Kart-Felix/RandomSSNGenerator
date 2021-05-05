#2021 Osaym Omar
#Inspired by online websites, as I wanted to see how they made their tool. Although, for the first three digits and possibly the middle two are most likely pulled from a list, and then the last 4 are auto generated. I don't want to accidentally make real SSN's, so this is not going to be done.
###DISCLAIMER###
#This script does not actually make real SSN's. If it does, then blame your computer because that's the one that did it.
#Thanks for using my bullshit script enjoy making bogus SSN's!

import random

one = str(random.randint(0,9))
two = str(random.randint(0,9))
three = str(random.randint(0,9))
#dash
four = str(random.randint(0,9))
five = str(random.randint(0,9))
#dash
six = str(random.randint(0,9))
seven = str(random.randint(0,9))
eight = str(random.randint(0,9))
nine = str(random.randint(0,9))

print (one + two + three + "-" + four + five + "-" + six + seven + eight + nine)