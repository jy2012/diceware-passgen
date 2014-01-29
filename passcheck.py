#!/usr/bin/env python

# by Jonathan Yuan
# https://github.com/jy2012/

import re
import math

def check_password_strength(password):
    n = 0                   # number of possible symbols
    l = len(password)       # length of password

    alpha_lower_flag = False
    alpha_upper_flag = False
    numeric_flag = False
    ascii_symbols = False

    for character in password:
        if re.search('[a-z]', character) and alpha_lower_flag == False:
            n += 26 
            alpha_lower_flag = True
        elif re.search('[A-Z]', character) and alpha_upper_flag == False:
            n += 26
            alpha_upper_flag = True
        elif re.search('[0-9]', character) and numeric_flag == False:  
            n += 10
            numeric_flag = True
        elif re.search('\s|[!-~]', character) and ascii_symbols == False:
            n += 33
            ascii_symbols = True
        else:
            continue

    print (n)
    print (l)
    info_entropy = l * (math.log(n) / math.log(2))
    return info_entropy

password = str(input("Enter password: "))
print (check_password_strength(password))
