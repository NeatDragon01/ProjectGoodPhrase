# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 13:09:21 2025

@author: Jeremy.Graue
"""

# 04/29/25 - Notes for later: Issue with variables, need to fix, causing conflict with passphrase generator code.

import random
import tkinter as tk
# Gets information from PassphraseProject.py
def generate_passphrase():
    global num_words_entry, capitalize_check, numbers_check, num_pos_var, symbols_var, custom_symbols_entry, defaultsym_var, sym_pos_var
    num_words_entry = num_words_entry.get()
    capitalize_check = capitalize_var.get()
    numbers_check = numbers_var.get()
    num_pos_var = num_pos_var.get()
    symbols_var = symbols_var.get()
    custom_symbols_entry = custom_symbols_entry.get()
    defaultsym_var = defaultsym_var.get()
    sym_pos_var = sym_pos_var.get()
    
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
        
    for word in passphrase_words:
        if capitalize == "y":
            final_passphrase.append(word.capitalize())
        else:
            final_passphrase.append(word)
            
    if include_numbers == "y":
        num_amount = int(input("How many sets of numbers do you want? :  "))
        num_pos = input("Where do you want the number to be placed? ([B]eginning/[M]iddle/[E]nd):  ").lower()
                
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
    pass

# Create the main window
window = tk.Tk()

# Set the title of the window
window.title("Passphrase Generator")

# Number of words
num_words_label = tk.Label(window, text="Enter the number of words: ")
num_words_label.pack()
num_words_entry = tk.Entry(window)
num_words_entry.pack()

# Checkbutton for Capitalization
capitalize_var = tk.BooleanVar()
capitalize_check = tk.Checkbutton(window, text="Capitalize Words", variable=capitalize_var)
capitalize_check.pack()

# Checkbutton for Numbers
numbers_var = tk.BooleanVar()
numbers_check = tk.Checkbutton(window, text="Include Numbers: ", variable=numbers_var)
numbers_check.pack()

# Radio buttons for Number Placement
num_pos_label = tk.Label(window, text="Number Placement: ")
num_pos_label.pack()

num_pos_var = tk.StringVar(value="beginning")
num_pos_beginning = tk.Radiobutton(window, text="Beginning", variable=num_pos_var, value="beginning")
num_pos_beginning.pack()
num_pos_middle = tk.Radiobutton(window, text="Middle", variable=num_pos_var, value="middle")
num_pos_middle.pack()
num_pos_end = tk.Radiobutton(window, text="End", variable=num_pos_var, value="end")
num_pos_end.pack()


# Checkbutton for Symbols
symbols_var = tk.BooleanVar()
symbols_check = tk.Checkbutton(window, text="Include Symbols: ", variable=symbols_var)
symbols_check.pack()

# Radiobutton for Symbol Placement
sym_pos_label = tk.Label(window, text="Symbol Placement:")
sym_pos_var = tk.StringVar(value="beginning")
sym_pos_beginning = tk.Radiobutton(window, text="Beginning", variable=sym_pos_var, value="beginning")
sym_pos_beginning.pack()
sym_pos_middle = tk.Radiobutton(window, text="Middle", variable=sym_pos_var, value="middle")
sym_pos_middle.pack()
sym_pos_end = tk.Radiobutton(window, text="End", variable=sym_pos_var, value="end")
sym_pos_end.pack()

#Entry for Custom Symbols
custom_symbols_label = tk.Label(window, text="Enter custom symbols (e.g., !@#$%^): ")
custom_symbols_label.pack()
custom_symbols_entry = tk.Entry(window)
custom_symbols_entry.pack()

# Checkbox for Default Symbols
defaultsym_var = tk.BooleanVar()
defaultsym_check = tk.Checkbutton(window, text="Use a List of Default Symbols", variable=defaultsym_var)
defaultsym_check.pack()

# Button to generate the passphrase
generate_button = tk.Button(window, text="Generate Passphrase!", command=generate_passphrase)
generate_button.pack()

# Label to display the generated passphrase (starts out empty)
result_label = tk.Label(window, text="")
result_label.pack()

# Start the Tkinter event loop (keeps the window open and responsive)
window.mainloop()