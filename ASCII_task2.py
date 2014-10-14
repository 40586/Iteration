#kieran burnett
#10-10-2014
#ASCII task 2

length = int(input("Please enter the length of password that you want: "))

import string
import random

count = length
while count != 0:
    print(random.choice(string.ascii_lowercase))
    count = count - 1



