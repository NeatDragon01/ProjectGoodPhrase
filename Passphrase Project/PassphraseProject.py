# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 09:58:21 2025

@author: Jeremy.Graue
"""

import random
open('C:/Users/Jeremy.Graue/ProjectGoodPhrase/Passphrase Project/EFF-long-word-list.txt',
     'r')
default_special = "~!@#$%^&*()-_=+?"
EFFdict = {

}

with open('C:/Users/Jeremy.Graue/ProjectGoodPhrase/Passphrase Project/EFF-long-word-list.txt', 'r') as file:
    for line in file:
        parts = line.strip().split('\t')
        if len(parts) == 2:
		#process each 'line' here
            EFFdict[parts[0]] = parts[1]
#In case of dictionary failure, uncomment this line. VVVVV            
#print("EFFdict length:", len(EFFdict))
        
num_rolls = 5
diceRoll = []
final_passphrase = []

num_words = input("Enter the desired length of the passphrase (number of words):  ")
capitalize = input("Do you need capital letters? (y/n):  ").lower()
include_numbers = input("Do you need numbers? (y/n):  ").lower()

    
try:
    num_words = int(num_words)
    
except ValueError:
    print("Invalid input. Please enter a whole number.")
    
else:
    passphrase_words = []
    for _ in range(num_words):
        diceRoll = [] #reset diceroll for each iteration
        for _ in range(num_rolls):
            roll = random.randint(1, 6)
            diceRoll.append(roll)
        
        rollList = "".join(map(str, diceRoll))
        passphrase_words.append(EFFdict[rollList])
    
    passphrase = " ".join(map(str, passphrase_words)) #join with spaces
  
              
for word in passphrase_words:
    if capitalize == "y":
        final_passphrase.append(word.capitalize())
    else:
        final_passphrase.append(word)
        
if include_numbers == "y":
    num_amount = int(input("How many sets of numbers do you want? :  "))
    num_pos = input("Where do you want the number to be placed? ([B]eginning/[M]iddle/[E]nd):  ").lower()
    rando_num_set = []
    
for _ in range(num_amount):
    random_number = random.randint(111, 999)
    
    if num_pos == "b":
        final_passphrase.insert(0, str(random_number))
    elif num_pos == "m":
        middle_index = len(final_passphrase) // 2
        final_passphrase.insert(middle_index, str(random_number))
    elif num_pos == "e":
        final_passphrase.append(str(random_number))
    else:
        print("Invalid placement option. Numbers not added.")
else:
    pass #User doesn't want numbers? Cool, do nothing.
    
include_symbols = input("Do you need symbols? (y/n): ").lower()
if include_symbols == "y":
    default_symbols = input("Do you want to use the default list of symbols? (y/n):  ")
    
    if default_symbols == "n":
        user_sym = input("Enter the symbols you would like to use: (e.g., !@#$): ")
        random_symbol = str(random.choice(user_sym))
        
    else:
        pass
    
    sym_pos = input("Where do you want the symbol to be placed? ([B]eginning/[M]iddle/[E]nd/[W]ord Separator):  ").lower()
    random_symbol = str(random.choice(default_special))
    
    if sym_pos == "b":
        final_passphrase.insert(0, str(random_symbol))
    elif sym_pos == "m":
        middle_index = len(final_passphrase) // 2
        final_passphrase.insert(middle_index, str(random_symbol))
    elif sym_pos == "e":
        final_passphrase.append(str(random_symbol))
    elif sym_pos == "w":
        final_passphrase = random_symbol.join(final_passphrase)
    else:
        print("Invalid placement option. Number not added.")
        
else:
    pass

print(final_passphrase)