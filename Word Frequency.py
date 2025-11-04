# Ask a user for a sentence and count how many times each character appears in the sentence
userinput = input("Please type a sentence: ").lower().split()#Convert the sentence to lowercase and splits them down word by word
wordcount = {}#create dictionary to hold them
for words in userinput:#loop for words 
    for characters in words:#loop for letters in each word
        wordcount[characters] = 1 + wordcount.get(characters, 0)#assigning the count to each word in given sentence

print(wordcount)#print out the results