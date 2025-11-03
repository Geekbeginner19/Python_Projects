#Creating a simple word dictionary just to test my skills
words = {
    "hello" : "an expression or gesture of greeting — used interjectionally in greeting, in answering the telephone, or to express surprise",
    "cat" : "a carnivorous mammal (Felis catus) long domesticated as a pet and for catching rats and mice",
    "dog" : " a carnivorous mammal (Canis familiaris) closely related to the gray wolf that has long been domesticated as a pet, occurs in a variety of sizes, colors, and coat types, and is sometimes trained to perform special tasks (such as herding, guarding, or acting as a service animal)",
    "mouse" : "any of numerous small rodents (as of the genus Mus) with pointed snout, rather small ears, elongated body, and slender tail",
}
endprompt = ""
while endprompt.lower() != "no":
    userinput = input("Please enter a word to get it meaning: ").lower()
    data_valid = False 
    while data_valid == False:#validating data
        try:
            userinput = int(userinput)#Tries to convert input into a number
            userinput = input("Numbers are not allowed. Please enter a word: ")#loop runs until a strings are entered
        except:
            data_valid = True#Inner loop ends when python interpreter gets here
    result = words.get(userinput.lower(), "Sorry, the word you typed is not available in this dictionary.\nPlease try another word: ")#Tries to get the key from the dictionary or prints an error message if the user input doesn't match the contents of the dictionary
    print(result)#Prints out the value if key entered is available 
    endprompt = input("Do you want to play again?\nPress ENTER to continue play\nType 'no' to quit: ").lower()#Keeps outta loop running unless user entered "no"
    

