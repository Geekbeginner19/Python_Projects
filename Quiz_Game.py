'''
CREATE A QUIZZING GAME. MAKE AN HTTP REQUEST TO THE OPEN TRIVIA API AT EACH ROUND TO GET
A NEW QUESTION AND PRESENT IT TO THE USER TO ANSWER. AT THE END OF EACH ROUND ASK THE USER
IF HE WANTS TO PLAY AGAIN. KEEP PLAYING FOREVER UNTIL THE USER TYPES 'QUIT'
DON'T FORGET TO TELL IF THE ANSWER IS CORRECT OR NOT AT EACH ROUND AND KEEP THE USER'S SCORE
'''


import requests
import json
import html
import random

while True:
    R = requests.get("https://opentdb.com/api.php?amount=1&category=27&difficulty=easy&type=multiple")
    loadToDict = json.loads(R.text) #Converts json to python dictionary
    questions = loadToDict["results"][0]["question"] #accessing the questions from API
    choices = loadToDict["results"][0]["incorrect_answers"] #accessing incorrect answers from API
    correctAnswer = loadToDict["results"][0]["correct_answer"]#acessing correct answers from API
    choices.append(correctAnswer)#adding correct answer to incorrect answers list
    random.shuffle(choices) #since append() adds the correct to the end of the list I'd to shuffle the whole list so the game is fair
    print("\n" + html.unescape(questions) + "\n")#displaying the questions
    options = 1
    for multiple_choice in choices:#loop for display the multiple choice answers
        print(str(options)+ "." + html.unescape(multiple_choice))
        options += 1
    #collecting user input
    Useranswer = input("\nEnter the number option of the answer: ").lower()       
    Useranswer = choices[int(Useranswer) - 1]
    #checking for the correct answer
    if (Useranswer.lower() == correctAnswer.lower()):
        print("Congratulations!, your answer is correct")
    else:
        print("Sorry, your answer is wrong, the correct answer is " + correctAnswer)
    #asking the user to see whether he wants to continue playing or quit
    userConfirm = input("\nDo you want to play again? Type 'no' to exit or press ENTER to play again: ").lower()
    if (userConfirm == "no"):
        break
    else:
        continue

#This is a simple program with no error handling.... so please just play by the rules :)
