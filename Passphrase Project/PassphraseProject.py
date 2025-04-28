import random
open('/Users/Jeremy.Graue/Documents/Passphrase Project/EFF-long-word-list.txt',
     'r')

EFFdict = {

}

with open('/Users/Jeremy.Graue/Documents/Passphrase Project/EFF-long-word-list.txt', 'r') as file:
	for line in file:
        parts = line.strip().split(' ')
        if len(parts) == 2
		#process each 'line' here
		EFFdict[parts[0]] = parts[1]
        
num_rolls = 5
diceRoll = []

num_words = input("Enter the desired length of the passphrase (number of words):")

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
        
        yourRoll = "".join(map(str, diceRoll))
        passphrase_words.append(EFFdict[yourRoll])
    
    passphrase = " ".join(map(str, passphrase_words)) #join with spaces
                        
print(passphrase)