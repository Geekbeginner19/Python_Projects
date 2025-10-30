'''
A simple game where the computer randomly selects a number, and the player has to guess it

REQUIREMENTS:
*The computer randomly selects a number between 1 and 10.
*The player has a limited number of tries (say, 7 attempts).
*After each guess, the program tells the player whether their guess is too high, too low, or correct.
*If the player guesses correctly, the game congratulates them and ends.
*If the player runs out of attempts, the game reveals the correct number.

BONUS CHALLENGE (OPTIONAL)
Add a difficulty level:
*Easy → 10 attempts
*Medium → 7 attempts
*Hard → 5 attempts
After the game ends, ask the player if they want to play again.
'''
import random
def game():
    print("Hello there, Welcome :)\nThis is a number guessing game.\nI pick a random number from 1 to 10 and you try to guess it:)")
    endgame = " "
    while endgame.lower() != "no":
        #Data Validation
        data_valid = False
        while data_valid == False: #checking data validation (Runs through most of the code)
            difficultylvl = input("\nSelect a difficulty level: \n1.Easy\n2.Medium\n3.Hard\n")
            try: #start of try and except block (Runs through most of the code)
                difficultylvl = int(difficultylvl) #trying to convert to integer
                if difficultylvl < 1 or difficultylvl > 3:
                    print("Please enter a valid option")
                else:
                    data_valid = True #if number is not within the range, this runs
            except:
                print("Alphabets are not allowed.")#if it's unable to convert to int, this runs
            #End of try and except block (Same Structure runs through the code)
        if (difficultylvl == 1):
            randNumber = random.randint(1, 10)
            userinput = "0"
            while (int(userinput) != randNumber):
                count = 0
                while count < 10:
                    data_valid = False
                    while data_valid == False:
                        userinput = input("Please guess the number: ")
                        try:
                            userinput = int(userinput)
                            if userinput < 1 or userinput > 10:
                                print("please enter within range of guess.")
                            else:
                                data_valid = True
                        except:
                            print("Alphabets are not allowed.")

                    if (int(userinput) == randNumber and count < 10):
                        print("Congratulations, you guess the number.")
                        break #breaks out of inner while loop to the next break
                    elif(int(userinput) < randNumber):
                        print("Wrong guess: Too low")
                    else:
                        print("Wrong guess: Too high")
                    count += 1
                    if count == 10:
                        print(f"Couldn't guess number in time :( the number was {randNumber}")
                        break #breaks out of inner while loop to the next break
                break #breaks out of outer while loop to the endgame variable
            endgame = input("End game?\nENTER - play again\nType 'no' - exit game ").lower()
        elif(difficultylvl == 2):
            randNumber = random.randint(1, 10)
            userinput = "0"
            while (int(userinput) != randNumber):
                count = 0
                while count < 7:
                    data_valid = False
                    while data_valid == False:
                        userinput = input("Please guess the number: ")
                        try:
                            userinput = int(userinput)
                            if userinput < 1 or userinput > 10:
                                print("please enter within range of guess.")
                            else:
                                data_valid = True
                        except:
                            print("Alphabets are not allowed.")

                    if (int(userinput) == randNumber and count < 7):
                        print("Congratulations, you guess the number.")
                        break #breaks out of inner while loop to the next break
                    elif(int(userinput) < randNumber):
                        print("Wrong guess: Too low")
                    else:
                        print("Wrong guess: Too high")
                    count += 1
                    if count == 7:
                        print(f"Couldn't guess number in time :( the number was {randNumber}")
                        break #breaks out of inner while loop to the next break
                break #breaks out of outer while loop to the endgame variable
            endgame = input("End game?\nENTER - play again\nType 'no' - exit game ").lower()
        else:
            randNumber = random.randint(1, 10)
            userinput = "0"
            while (int(userinput) != randNumber):
                count = 0
                while count < 5:
                    data_valid = False
                    while data_valid == False:
                        userinput = input("Please guess the number: ")
                        try:
                            userinput = int(userinput)
                            if userinput < 1 or userinput > 10:
                                print("please enter within range of guess.")
                            else:
                                data_valid = True
                        except:
                            print("Alphabets are not allowed.")
                            
                    if (int(userinput) == randNumber and count < 5):
                        print("Congratulations, you guess the number.")
                        break #breaks out of inner while loop to the next break
                    elif(int(userinput) < randNumber):
                        print("Wrong guess: Too low")
                    else:
                        print("Wrong guess: Too high")
                    count += 1
                    if count == 5:
                        print(f"Couldn't guess number in time :( the number was {randNumber}")
                        break #breaks out of inner while loop to the next break
                break #breaks out of outer while loop to the endgame variable 
            endgame = input("End game?\nENTER - play again\nType 'no' - exit game ").lower()
game()

