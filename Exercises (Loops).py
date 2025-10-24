'''
CREATE A PROGRAM THAT ASKS THE USER FOR 8 NAMES OF PEOPLE AND STORE THEM IN A LIST.
WHEN ALL THE NAMES HAVE BEEN GIVEN, PICK A RANDOM ONE AND PRINT IT
'''
import random
namesList = []
for names in range(8) :
    names = input("Please enter a name: ")
    namesList.append(names)
randomNumber = random.randint(0,7)
print(namesList[randomNumber])


'''
CREATE A GUESS GAME WITH THE NAMES OF THE COLORS. AT EACH ROUND PICK A RANDOM COLOR FROM
A LIST AND LET THE USER TRY TO GUESS IT. WHEN HE DOES IT, ASK IF HE WANTS TO PLAY AGAIN.
KEEP PLAYING UNTIL THE USER TYPES "NO"
'''

import random
colorList = ["blue", "red", "green", "yellow", "black", "purple", "violet", "white", "grey"]
while True:
    randomColor = random.randint(0, len(colorList) - 1)
    userguess = input("Guess the color I'm thinking about:)").lower()
    while True:
        if (userguess == colorList[randomColor]):
            print("Yaaaay..... you guessed it!")
            break
        else:
            userguess = input("Nope, Try Again:)").lower()       
    play_again = input("Do you wanna play again? Type 'no' to quit.").lower()
    if play_again == "no":
        break
print("Nice playing with you:)\nByee")

        
    
        
    
