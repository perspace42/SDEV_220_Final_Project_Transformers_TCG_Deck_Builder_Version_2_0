'''
Author: Scott Field
Version: 1.0
Name: Card_Total
Date: 05/11/2023
Purpose: Create a table to track the number of cards added to the deck and the
number of points spent by adding those cards.
'''

from PyQt5 import QtCore
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

#A table seemed the most logical widget to place the data in
class Total(QTableWidget):
    def __init__(self,parentWidget):
        super().__init__(parentWidget)

        #Variables to Track Card Data
        self.numBotCards = 0
        self.numBattleCards = 0
        self.numStratagemCards = 0

        self.pointsBotCards = 0
        self.pointsBattleCards = 0
        self.pointsStratagemCards = 0

        self.pointsTotal = 0

        #Set Table Info
        self.setColumnCount(2)
        self.setRowCount(7)

        #Set Battle Cards Data Tracker
        self.setItem(0, 0, QTableWidgetItem("Battle Cards:"))
        self.setItem(0, 1, QTableWidgetItem("0/40"))

        self.setItem(1, 0, QTableWidgetItem("Total Points:"))
        self.setItem(1, 1, QTableWidgetItem("0/25"))

        self.setItem(2, 0, QTableWidgetItem("Battle Points:"))
        self.setItem(2, 1, QTableWidgetItem("0"))

        self.setItem(3, 0, QTableWidgetItem("Bot Cards:"))
        self.setItem(3, 1, QTableWidgetItem("0"))

        self.setItem(4, 0, QTableWidgetItem("Bot Points:"))
        self.setItem(4, 1, QTableWidgetItem("0"))

        self.setItem(5, 0, QTableWidgetItem("Stratagem Cards:"))
        self.setItem(5, 1, QTableWidgetItem("0"))

        self.setItem(6, 0, QTableWidgetItem("Stratagem Points:"))
        self.setItem(6, 1, QTableWidgetItem("0"))

        
    #Add a value (positive or negative) to the correct row,column in the table
    #determined by dataType
    def addValue(self,value,dataType):
        #If adding cards to the table
        if (dataType == "Battle Card"):
            self.numBattleCards += value

            #Set the column and row to add the card
            row = 0
            column = 1
            
            #Set the string to add to the table
            dataString = str(self.numBattleCards) + "/40"

            #Set the string to the table location       
            self.setItem(row,column, QTableWidgetItem(dataString))

        elif(dataType == "Bot Card"):
            self.numBotCards += value

            #Set the column and row to add the card
            row = 3
            column = 1
            
            #Set the string to add to the table
            dataString = str(self.numBotCards)

            #Set the string to the table location       
            self.setItem(row,column, QTableWidgetItem(dataString))

        elif(dataType == "Stratagem Card"):
            self.numStratagemCards += value

            #Set the column and row to add the card
            row = 5
            column = 1

            #Set the string to add to the table
            dataString = str(self.numStratagemCards)

            #Set the string to the table location       
            self.setItem(row,column, QTableWidgetItem(dataString))

        #If adding points to the table
        else:
            if(dataType == "Battle Point"):
                self.pointsBattleCards += value

                #Set the column and row to add the card
                row = 2
                column = 1
            
                #Set the string to add to the table
                dataString = str(self.pointsBattleCards)

                #Set the string to the table location       
                self.setItem(row,column, QTableWidgetItem(dataString))
            
            elif(dataType == "Bot Point"):
                self.pointsBotCards += value

                #Set the column and row to add the card
                row = 4
                column = 1
            
                #Set the string to add to the table
                dataString = str(self.pointsBotCards)

                #Set the string to the table location       
                self.setItem(row,column, QTableWidgetItem(dataString))

            #Stratagem Point
            else:
                self.pointsStratagemCards += value

                #Set the column and row to add the card
                row = 6
                column = 1
            
                #Set the string to add to the table
                dataString = str(self.pointsStratagemCards)

                #Set the string to the table location       
                self.setItem(row,column, QTableWidgetItem(dataString))

            #Increment Added Points To Total
            row = 1
            column = 1
            self.pointsTotal += value
            dataString = str(self.pointsTotal) + "/25"
            
            #Set the string to the total table location (This happens every time a card is added or removed)
            self.setItem(row,column, QTableWidgetItem(dataString))



   
    