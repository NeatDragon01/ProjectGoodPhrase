# -*- coding: utf-8 -*-
"""
Project Good Phrase

Created on Tue Apr 29 13:09:21 2025

@author: Jeremy.Graue
"""

# 04/29/25 - Notes for later: Issue with variables, need to fix, causing conflict with passphrase generator code.
# 05/01/25 - Issues with tkinter, final_passphrase not printing to window.

import random
import tkinter as tk
import tkinter.font as tkFont
# Gets information from PassphraseProject.py
def generate_passphrase():
    global num_words_entry, cap_check, num_check, num_pos_var, sym_var, custom_symbols_entry, defaultsym_var, sym_pos_var, result_label
    num_words_str = num_words_entry.get()
    max_char_str = max_char_entry.get()
    cap_check = capitalize_var.get()
    num_check = num_var.get()
    num_pos = num_pos_var.get()
    symbol = sym_var.get()
    user_sym = custom_symbols_entry.get()
    defaultsym = defaultsym_var.get()
    sym_pos = sym_pos_var.get()
    
    default_special = "~!@#$%^&*()-_=+?"
    EFFdict = {

    }
    try:
        with open('C:/Users/Jeremy.Graue/ProjectGoodPhrase/EFF-Long-Word-List.txt', 'r') as file:
            # Uncomment if having trouble with word list. VVVVV
            #print("File opened successfully!")
            for line in file:
                parts = line.strip().split('\t')
                if len(parts) == 2:
    		#process each 'line' here
                    EFFdict[parts[0]] = parts[1]
    #In case of dictionary failure, uncomment this line. VVVVV            
    #print("EFFdict length:", len(EFFdict))
    except FileNotFoundError: 
        result_entry.config(state="normal")
        result_entry.delete(0, tk.END)
        result_entry.insert(0, "Error: EFF word list file not found! Check file path.")
        result_entry.config(state="readonly")
        return # Exit function if the file is not found.
            
    num_rolls = 5
    diceRoll = []
    final_passphrase = []
    
    try:
        max_length = int(max_char_str)
        if max_length <= 0:
            result_entry.config(state="normal")
            result_entry.delete(0, tk.END)
            result_entry.insert(0, "Maximum length must be a positive number.")
            result_entry.config(state="readonly")
            return
    except:
            result_entry.config(state="normal")
            result_entry.delete(0, tk.END)
            result_entry.insert(0, "Invalid input. Please enter a whole number.")
            result_entry.config(state="readonly")
            return

    try:
        num_words = int(num_words_str)
        
    except ValueError:
        result_entry.config(state="normal")
        result_entry.delete(0, tk.END)
        result_entry.insert(0, "Invalid input. Please enter a whole number.")
        result_entry.config(state="readonly")
        return
        
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
        if cap_check == True:
            final_passphrase.append(word.capitalize())
        else:
            final_passphrase.append(word)
    num_amount = 0 # If the if statement is a no, it atleast have a value to add.
    if num_check == True:
        num_amount = 1
                        
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
            result_entry.config(state="normal")
            result_entry.delete(0, tk.END)
            result_entry.insert(0, "Invalid placement option. Numbers not added.")
            result_entry.config(state="readonly")
    else:
        pass #User doesn't want numbers? Cool, do nothing.
        
        if symbol == True:

            if defaultsym == False:
                if user_sym: # Only choose if the string is not empty
                    random_symbol = str(random.choice(user_sym))
                else:
                    pass
            else: # Fallback to default if user enters nothing
                random_symbol = str(random.choice(default_special))

            if sym_pos == "b": # Symbol position radial selection
                final_passphrase.insert(0, str(random_symbol))
            elif sym_pos == "m":
                middle_index = len(final_passphrase) // 2
                final_passphrase.insert(middle_index, str(random_symbol))
            elif sym_pos == "e":
                final_passphrase.append(str(random_symbol))
            elif sym_pos == "w":
                final_passphrase = random_symbol.join(final_passphrase)
            else:
                result_entry.config(state="normal")
                result_entry.delete(0, tk.END)
                result_entry.insert(0, "Invalid symbol placement option. Symbol not added.")
                result_entry.config(state="readonly")
                
        else:
            pass
        
        # The Max Character Limit Check
        final_passphrase = " ".join(final_passphrase)
        if max_length > 0 and len(final_passphrase) > max_length:
                final_passphrase = final_passphrase[:max_length]
                result_entry.config(state="normal") 
                result_entry.delete(0, tk.END)
                result_entry.insert(0, f"(Truncated) {final_passphrase}")
                result_entry.config(state="readonly")
        else:
            result_entry.config(state="normal") 
            result_entry.delete(0, tk.END)
            result_entry.insert(0, final_passphrase)
            result_entry.config(state="readonly")
            return
       

# Create the main window
window = tk.Tk()

# Set the title of the window
window.title("Passphrase Generator")

large_font = tkFont.Font(family="Verdana", size=16)

# Number of words
num_words_label = tk.Label(window, text="Enter the number of words: ")
num_words_label.pack()
num_words_entry = tk.Entry(window)
num_words_entry.pack()

max_char_label = tk.Label(window, text="Maximum Passphrase Length:  ")
max_char_label.pack()
max_char_entry = tk.Entry(window)
max_char_entry.pack()

# Checkbutton for Capitalization
capitalize_var = tk.BooleanVar()
capitalize_check = tk.Checkbutton(window, text="Capitalize Words", variable=capitalize_var)
capitalize_check.pack()

# Checkbutton for Numbers
num_var = tk.BooleanVar()
num_check = tk.Checkbutton(window, text="Include Numbers: ", variable=num_var)
num_check.pack()

# Radio buttons for Number Placement
num_pos_label = tk.Label(window, text="Number Placement: ")
num_pos_label.pack()

num_pos_var = tk.StringVar(value="b")
num_pos_beginning = tk.Radiobutton(window, text="Beginning", variable=num_pos_var, value="b")
num_pos_beginning.pack()
num_pos_middle = tk.Radiobutton(window, text="Middle", variable=num_pos_var, value="m")
num_pos_middle.pack()
num_pos_end = tk.Radiobutton(window, text="End", variable=num_pos_var, value="e")
num_pos_end.pack()


# Checkbutton for Symbols
sym_var = tk.BooleanVar()
sym_check = tk.Checkbutton(window, text="Include Symbols: ", variable=sym_var)
sym_check.pack()

# Radiobutton for Symbol Placement
sym_pos_label = tk.Label(window, text="Symbol Placement:")
sym_pos_var = tk.StringVar(value="b")
sym_pos_beginning = tk.Radiobutton(window, text="Beginning", variable=sym_pos_var, value="b")
sym_pos_beginning.pack()
sym_pos_middle = tk.Radiobutton(window, text="Middle", variable=sym_pos_var, value="m")
sym_pos_middle.pack()
sym_pos_end = tk.Radiobutton(window, text="End", variable=sym_pos_var, value="e")
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
result_entry = tk.Entry(window, width=40, justify="center", font=large_font) # Adjust width as needed.
result_entry.config(state="readonly") # Makes the entry section read-only.
result_entry.pack(ipady=20) # Adjusts the height of the result box.

# Start the Tkinter event loop (keeps the window open and responsive)
window.mainloop()