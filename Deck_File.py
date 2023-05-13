'''
Author: Scott Field
Version: 1.0
Name: Deck_File
Date: 05/12/2023
Purpose: Create the functions to save cards added to the deck to a file and pull
those cards from the file to the deck
'''
from Card_Data import *

#Function To Open A new TXT File
def openFile(fileName = ""):
    if (fileName == ""):
        fileName == "newDeck.txt"
    
    
    file = open(fileName,"w")
    file.close()

    return fileName

#using the list of cards within each treeview, save the added cards to the file
#file assumes that if a parameter is None, their is no data of that type to save
#battle Data will store two lists in a tuple
#[0] will be the card data
#[1] will be the amount of cards added
def saveFile(fileName,botData = None, battleData = None, stratagemData = None):
    #open the file
    file = open(fileName,"w")

    #if their is any data to write
    if (botData != None):
        #write a header to mark which data is being written
        file.write("Bot Cards Header:\n")
        #iterate across the data
        for index in range(len(botData)):
            #store each card with its unique image file path
            file.write(botData[index].dataDict['path'] + "\n")
        
        file.write("Bot Cards Footer\n")

    #if their is any data to write
    if (stratagemData != None):
        #write a header to mark which data is being written
        file.write("Stratagem Cards Header:\n")
        #iterate across the data
        for index in range(len(stratagemData)):
            #store each card with its unique image file path
            file.write(stratagemData[index].dataDict['path'] + "\n")

        file.write("Stratagem Cards Footer\n")

    #if their is any data to write
    if (battleData != None):
        #split battleData into two parallel lists
        battleCards = battleData[0] #this one stores the card data
        battleQuantity = battleData[1] #this one stores the number of times that card is in the deck
        #write a header to mark which data is being written
        file.write("Battle Cards Header:\n")
        #iterate across the data
        for index in range(len(battleCards)):
            #store each card with its unique image file path
            file.write(battleCards[index].dataDict['path'])
            #store the amount each card is within the deck
            file.write("(" + str(battleQuantity[index]) + ")\n")

        file.write("Battle Cards Footer")

    #close the file
    file.close()

def readFile(fileName):
    #initialize data storage lists
    botData = []
    battleCards = []
    battleQuantity = []
    stratagemData = []

    #open file
    file = open(fileName,"r")
    #convert file into list
    fileLines = file.read().splitlines()
    #close file immediatly after reading
    file.close()
   

    #Remove all newline characters
    for index in range(len(fileLines)):
        #remove newline character if it is present
        fileLines[index].strip("\n")
    
    #print the data within the file
    #print(fileLines)

    #If file contains bot card data
    if (fileLines[0] == "Bot Cards Header:"):
        counter = 1
        end = fileLines.index('Bot Cards Footer')
        #while the end of the bot section hasn't been reached, continue iteration
        for counter in range(counter,end):
            botData.append(fileLines[counter])
            #print(fileLines[counter])
    else:
        botData = None
    
    #If file contains stratagem card data
    if ("Stratagem Cards Header:" in fileLines):
        counter = fileLines.index("Stratagem Cards Header:") + 1
        end = fileLines.index('Stratagem Cards Footer') 
        for counter in range(counter,end):
            stratagemData.append(fileLines[counter])
            #print(fileLines[counter])
    else:
        stratagemData = None

    #If file contains battle card data
    if ("Battle Cards Header:" in fileLines):
        counter = fileLines.index("Battle Cards Header:") + 1
        end = fileLines.index("Battle Cards Footer") 
        for counter in range(counter,end):
            #get the quantity from the string
            battleQuantity.append(fileLines[counter][-2])
            #get the card name from the string
            battleCards.append(fileLines[counter][0:-3])
            #print(fileLines[counter][0:-3],(fileLines[counter])[-2])

        #Set BattleData
        battleData = (battleCards,battleQuantity)
    else:
        battleData = None
    
    #print the results of reading the file
    print("Bot Cards:\n" , botData , "\n")
    print("Battle Cards:\n",battleData,"\n")
    print("Stratagem Cards:\n",stratagemData,"\n")

    return (botData,battleData,stratagemData)
    
    

#convert a list of path strings to a list of cards by using the path strings to find the correct cards in the complete card list
def cardsFromText(cardList,completeCardList):
    for outer in range(len(cardList)):
        for inner in range(len(completeCardList)):
            currentCard = completeCardList[inner]
            currentPath = cardList[outer]
            #if the path string matches, then the correct card has been found
            if currentPath == currentCard.dataDict['path']:
                cardList[outer] = currentCard
                #if the card has been found return to the outer loop
                break

    #return the list of cards
    return cardList
