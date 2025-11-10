# 🔥 Python Project of the Day:
# 🎲 Dice Rolling Simulator

# 🎯 Goal:
# Create a simple dice roller program that simulates rolling one or more dice and shows random results each time the user rolls.

# 🧱 Requirements:

# When the program runs, show this menu:
# --- Dice Rolling Simulator ---
# 1. Roll one die
# 2. Roll multiple dice
# 3. Quit

# ⚙️ Features:
# 1. Roll one die

# When chosen, generate a random number between 1 and 6 using:
# import random
# roll = random.randint(1, 6)


# Display something like:
# 🎲 You rolled a 4!

# 2. Roll multiple dice
# Ask the user how many dice to roll.
# Display all results on one line, e.g.:
# You rolled: [2, 5, 1]
# Total: 8

# 3. Quit
# Exit gracefully with a goodbye message.

import random #Importing Random module to make random draws of the dice

def one_roll():
    roll = random.randint(1, 6)#Picking a random number from 1 to 6
    print(f"🎲 You rolled a {roll}!")

def multiple_rolls():
    roll_list = []#Creating a list to store multiple outcomes of the dice
    while True:#Infinte Loop        
        rollNumber = input("How many dices do you want to roll?: ")
        try:
            rollNumber = int(rollNumber)#Try the integer conversion
            for dice in range(rollNumber):#Looping this this number of times the user wants to roll the dice
                roll = random.randint(1,6)
                roll_list.append(roll)#Adding each result of the roll to a list
            print(f"🎲 You rolled {roll_list}\nTotal : {sum(roll_list)}")
            break
        except:
            print("Please enter a valid number.")#If integer conversion doesn't work then it's likely an alphabet or something

while True:
    options = input("\n--- Dice Rolling Simulator ---\n1. Roll one die\n2. Roll multiple dice\n3. Quit\nChoose an option>>> ")
    try:#Error handlimg block
        options = int(options)
        if options < 1 or options > 3:#checking if the input is not with the range less than option 1 OR more than option 3
            print("Please enter an option within the range\n")#print this error message if option chosen is out of range
        else:
            if options == 1:
                one_roll()
            elif(options == 2):
                multiple_rolls()
            elif(options == 3):
                print("Goodbye.... Thanks for stopping by!")#Nice Exit Message
                break#exit the infinite loop whenthe user wants to quit the game
    except:
        print("Please enter a valid option\n")#Display this error message if user typed in an alphabet or decimals instead of a nummber



