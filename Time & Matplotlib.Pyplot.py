'''
CREATE A PROGRAM THAT HELPS A USER TYPE FASTER. GIVE HIM A WORD AND ASK HIM TO WRITE IT FIVE
TIMES. CHECK HOW MANY SECONDS IT TOOK HIM TO TYPE THE WORD AS EACH ROUND.
IN THE END, TELL THE USER HOW MANY MISTAKES WERE MADE AND SHOW A CHART WITH THE TYPING SPEED
EVOLUTION DURING THE 5 ROUNDS.
'''
#Importing the neccessary Libraries
import time as t
import matplotlib.pyplot as mplib

#starting the game
print("Hello!, this is a program that will help you type faster!")
print("You're about to type the word 'programming' five times: ")
print("countdown!")
count = 5
while count > 0: #small loop for countdown
    t.sleep(1)
    print(str(count))
    count -= 1

mistakes = 0
timeSpeedEvo = []
for timeToType in range(5): #loop for checking the speed of every typing round and checking mistakes too
    t1 = t.time()
    userType = input("Type the word:")
    t2 = t.time()
    tfinal = round((t2 - t1))
    timeSpeedEvo.append(tfinal)
    print("time taken: " + str(tfinal) + "seconds")
    if (userType.lower() != "programming"):
        mistakes += 1
    else:
        continue
#displying mistakes done if any to the user
print("These are the number of mistakes made: " + str(mistakes))

#game round
gameround = 1
gameroundlist = []
for timespeed in timeSpeedEvo: #small loop for displaying game rounds with typing speed
    print("Round " + str(gameround) +":"+ str(timespeed) + "seconds")
    gameroundlist.append(gameround)
    gameround += 1

#using the two lists created for gamerounds and typing speed to plot the chart
mplib.plot(gameroundlist, timeSpeedEvo)
legend = ["1", "2", "3", "4", "5"]
mplib.xticks(gameroundlist, legend)
mplib.title("Your typing evolution")
mplib.xlabel("Game Round")
mplib.ylabel("Time")
mplib.show() #displaying chart results




