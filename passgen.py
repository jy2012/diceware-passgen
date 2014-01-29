#!/usr/bin/env python 

# by Jonathan Yuan
# https://github.com/jy2012/

import random
import math

word_list = {}

def load_diceware_file():
    try:
        diceware_file = open("diceware.wordlist.asc")
    except IOError:
        print ("Error reading diceware word list.")
    for line in diceware_file:
        combo, word = line.split()
        word_list[combo] = word

def generate_word():
    dice_roll = ""
    for number in range(1,6): 
        random.seed()
        dice_roll += str(random.randint(1,6))
    return word_list[dice_roll]

def generate_password(password_length = 7):
    password = ""
    for i in range(0, password_length):
        password += generate_word() + " "
    return password

def check_password_strength(info_entropy=0):
    info_entropy = int(info_entropy)
    if info_entropy < 28:
        return "Very Weak"
    elif info_entropy in range(28,36):
        return "Weak"
    elif info_entropy in range(36,60):
        return "Reasonable"
    elif info_entropy in range(60,128):
        return "Strong"
    else:
        return "Very Strong"

####################################################

print ("Diceware Password Generator")
print ("---------------------------")

load_diceware_file()

while True:
    try:
        password_length = int(input("Enter the length (in words) of the password to generate: "))
    except ValueError:
        print ("Error: You must enter a numerical value.")
        continue

    if password_length < 1:
        print ("Error: Length must be at least 1.")
    else:
        break

generated_password = generate_password(password_length)
info_entropy = password_length * (math.log(7776) / math.log(2))

print ("---------------------------")
print ("Password:\t\t{0}".format(generated_password))
print ("Information entropy:\t{0}".format(info_entropy))
print ("Strength:\t\t" + check_password_strength(info_entropy))

