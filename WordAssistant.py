# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 21:57:48 2018

@author: Raymond Adams
"""

#Option 1 - Word valid or not
def lookup_word(word, file):
    #Allows me to open and close files in a single block
    with open(file) as f1:
        for line in f1:
            #strip() removes all whitespace at the start and end of a string
            if word == line.strip():
                return True
        return False

#Option 2 - Suggested word list(only)
def suggest(input2):
    t1 = set(input2)
    lines = []
    
    with open("C:/Users/Radam/PythonProject2/wordlist.txt", newline='') as f1:
        for line in f1:
            lines.append(line.strip())

        for i in range(len(lines)):
            #Check if the users input is a subset of the any of the words but only if the word is equal to or less than the users input
            if t1.issubset(lines[i]) and len(input2) >= len(lines[i]):
                print(lines[i])
            else:
                continue
    
#print(suggest("AARGH"))


#This method could have been an alternative fucntion to suggest(). However, I could not determine how to turn the entire text file into a list and loop through each index.
#def is_contained(lista, listb):
#    for ele in lista:
#        if ele not in listb:
#            return False
#        elif ele in listb:
#            return True
#
#print(is_contained("R,A,D,T,E","T,R,A,D,E"))    

#Option 3 - Suggested word list along with score for each word
def suggested_score(input3):
    t1 = set(input3)
    lines = []
    
    with open("C:/Users/Radam/PythonProject2/wordlist.txt", newline='') as f1:
        for line in f1:
            lines.append(line.strip())

        for i in range(len(lines)):
            count = 0
            #Check if the users input is a subset of the any of the words but only if the word is equal to or less than the users input
            if t1.issubset(lines[i]) and len(input3) >= len(lines[i]):
                for letter in lines[i]:
                    if letter in "AEILNORSTU":
                        count += 1
                    elif letter in "DG":
                        count += 2
                    elif letter in "BCMP":
                        count += 3
                    elif letter in "FHVWY":
                        count += 4
                    elif letter in "K":
                        count += 5
                    elif letter in "X":
                        count += 8
                    elif letter in "Z":
                        count += 10
                    else:
                        count += 0
                print(count, lines[i])
            else:
                continue

#Option 4 - List the word(s) with highest score
def highest_score(input4):
    t1 = set(input4)
    lines = []
    
    with open("C:/Users/Radam/PythonProject2/wordlist.txt", newline='') as f1:
        for line in f1:
            lines.append(line.strip())

        for i in range(len(lines)):
            count = 0
            #Check if the users input is a subset of the any of the words but only if the word is equal to or less than the users input
            if t1.issubset(lines[i]) and len(input4) >= len(lines[i]):
                for letter in lines[i]:
                    if letter in "AEILNORSTU":
                        count += 1
                    elif letter in "DG":
                        count += 2
                    elif letter in "BCMP":
                        count += 3
                    elif letter in "FHVWY":
                        count += 4
                    elif letter in "K":
                        count += 5
                    elif letter in "X":
                        count += 8
                    elif letter in "Z":
                        count += 10
                    else:
                        count += 0
                dicta = {lines[i]: count}
                num = count
                #This only returns one of the keys although there may be more
                maximum = max(dicta, key=dicta.get)
                #print(count, lines[i])
            else:
                continue
       
        print(num, maximum)

    

def assistant():
    while input != "5":
        print("Welcome to the Word Assistant!\n")
        print("Option 1: Word Validity Check")
        print("Option 2: Suggested Word List")
        print("Option 3: Suggested Word List with Scores")
        print("Option 4: Words with Highest Scores")
        print("Option 5: Exit")
        
        choice=input("Enter the option of your choice: ")
        
        if choice in "1":
            input1 = input("Enter your word: ").upper()
            print(lookup_word(input1, "C:/Users/Radam/PythonProject2/wordlist.txt"))
        elif choice in "2":
            input2 = input("Enter your word: ").upper()
            print(suggest(input2))
        elif choice in "3":
            input3 = input("Enter your word: ")
            suggested_score(input3)
        elif choice in "4":
            input4 = input("Enter your word: ")
            highest_score(input4)
        #Option 5 - Quit or Exit     
        elif choice in "5":
            print("Exiting...")
            return
        
        print()
assistant()