'''
Author: Scott
Version: 2.1
Name: Card_Selection
Date: 05/07/2023
Purpose: Create a CardView class to add a Treeview for viewing cards to be added to the UI.py file
'''
from PyQt5.QtCore import Qt,QModelIndex
from PyQt5.QtGui import QStandardItemModel, QBrush, QColor
from PyQt5.QtWidgets import  QTreeView, QAbstractItemView

from Read_Database import *

#Function To Add bot cards to treeview data model
def treeBotCards(model,list):
    for i in range(len(list)):
        #Get First Card
        currentCard = list[i]

        #Get Name and Cost
        fullName = currentCard.dataDict['name'] + " " + currentCard.dataDict.get('subName',"")
        cost = currentCard.dataDict['cost']

            
        #Insert at Index 0
        model.insertRow(0)
        #Insert Full Name Of The Bot
        model.setData(model.index(0, 0), fullName)
        #Insert Cost Of The Bot
        model.setData(model.index(0, 1), cost)
            
        #Change Bot Background Color Based On Loyalty
        #initialize color values for background color
        r = 0
        g = 0
        b = 0

        #if the bot is an Autobot, set the background color values to red
        if (currentCard.dataDict['loyalty'] == "Autobot"):
            r = 178
            g = 0
            b = 0
        #if the bot is a Decepticon, set the background color values to purple
        elif(currentCard.dataDict['loyalty'] == "Decepticon"):
            r = 67
            g = 0
            b = 67
        #Otherwise the bot is a Mercenary, set the background color values to dark grey    
        else:
            r = 51
            g = 51
            b = 51
            
        #Add Color To Both Columns

        #Add Color To Name Column
        model.setData(model.index(0, 0), QBrush(QColor(r,g,b)), Qt.BackgroundRole)
        #Add Color To Cost Column
        model.setData(model.index(0, 1), QBrush(QColor(r,g,b)), Qt.BackgroundRole)

    #return data model
    return model
        
#Function To Add battle cards to treeview data model
def treeBattleCards(model,list):
    for i in range(len(list)):
        #Get First Card
        currentCard = list[i]

        #Get Name and Cost
        fullName = currentCard.dataDict['name']
        cost = currentCard.dataDict['cost']

            
        #Insert at Index 0
        model.insertRow(0)
        #Insert Full Name Of The Battle Card
        model.setData(model.index(0, 0), fullName)
        #Insert Cost Of The Battle Card
        model.setData(model.index(0, 1), cost)
            
        #Change Battle Card Background Color Based On Loyalty
        #initialize color values for background color
        r = 0
        g = 0
        b = 0

        #if the card is an Action, set the background color values to white
        if (currentCard.dataDict['cardType'] == "Action"):
            r = 255
            g = 255
            b = 255
        #if the card is an Secret Action, set the background color values to dark grey
        elif(currentCard.dataDict['cardType'] == "Secret Action"):
            r = 51
            g = 51
            b = 51
        #if the card is an Upgrade Determine its subType by looking at its side, then set its colors accordingly
        else:
            #If the card is an Weapon set the background color values to an orange
            if (currentCard.sideList[0].dataDict['subType'] == "Weapon"):
                r = 230
                g = 149
                b = 0
            #If the card is an Armor set the background color to a light cyan
            elif(currentCard.sideList[0].dataDict['subType'] == "Armor"):
                r = 0
                g = 255
                b = 255
            #If the card is an Utility set the background color values to light grey
            elif(currentCard.sideList[0].dataDict['subType'] == "Utility"):
                r = 128
                g = 128
                b = 128
            #If the card is an Weapon Armor set the background color values to light green
            else:
                r = 115
                g = 202
                b = 128
        
        
            
        #Add Color To Both Columns

        #Add Color To Name Column
        model.setData(model.index(0, 0), QBrush(QColor(r,g,b)), Qt.BackgroundRole)
        #Add Color To Cost Column
        model.setData(model.index(0, 1), QBrush(QColor(r,g,b)), Qt.BackgroundRole)

    #return data model
    return model

#Function To Add stratagem cards to treeview data model (stratagem cards are not color coded)
def treeStratagemCards(model,list):
    for i in range(len(list)):
        #Get First Card
        currentCard = list[i]

        #Get Name and Cost
        fullName = currentCard.dataDict['name']
        cost = currentCard.dataDict['cost']

            
        #Insert at Index 0
        model.insertRow(0)
        #Insert Full Name Of The Battle Card
        model.setData(model.index(0, 0), fullName)
        #Insert Cost Of The Battle Card
        model.setData(model.index(0, 1), cost)

    #return data model
    return model

class CardView(QTreeView):
    #Widget must be a QtWidgets.Qwidget
    def __init__(self,widget):
        super().__init__(widget)

        #Create Treeview Items
        #remove left tab space from treeview
        self.setRootIsDecorated(False)
        #prevent user from editing treeview items (can still select them)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        #create data storage container for treeview
        self.model = self.createDataModel(self)
        #add data storage container to treeview
        self.setModel(self.model)

        #initialize card data list to empty this list will store the cards currently shown within the treeview
        self.cardData = []

        #add event listener for treeview when treeview is clicked
        self.clicked.connect(self.on_clicked)


    def createDataModel(self,quantity = 2):
        #Set Column Headers
        model = QStandardItemModel(0, 2)
        model.setHeaderData(0, Qt.Horizontal, "Name")
        model.setHeaderData(1, Qt.Horizontal, "Cost")

        #If there is need for a third column, add it
        if (quantity == 3):
            model.setHeaderData(2,Qt.Horizontal, "Quantity")
        
        #return data model
        return model
    
    def addData(self,model,list):
        #Add Data From List To Columns (if the given list contains any values)
        if (len(list) > 0):
            #Add Cards To Card List
            self.cardData = list
            #Get First Card
            currentCard = list[0]

            #Get Card Type

            #If Card Type reveals data to contain bot cards, set the data model accordingly
            if (currentCard.dataDict['cardType'] in ("Battle Master", "BotPiece", "Combiner", "TitanMaster Head", "TitanMaster Body", "Multiform", "Bot")):
                model = treeBotCards(model,list)

                #Set Column Width (Must Be Set After Adding Data)
                #Set Name Column Width
                self.setColumnWidth(0,300)
                #Set Cost Column Width
                self.setColumnWidth(1,5)

            #If Card Type reveals data to contain battle cards, set the data model accordingly
            elif(currentCard.dataDict['cardType'] in ("Upgrade", "Action", "Secret Action")):
                model = treeBattleCards(model,list)

                #Set Column Width (Must Be Set After Adding Data)
                #Set Name Column Width
                self.setColumnWidth(0,250)
                #Set Cost Column Width
                self.setColumnWidth(1,5)

            #Otherwise Card Type must be a Stratagem, set the data model accordingly
            else:
                model = treeStratagemCards(model,list)

                #Set Column Width (Must Be Set After Adding Data)

                #Set Name Column Width
                self.setColumnWidth(0,200)
                #Set Cost Column Width
                self.setColumnWidth(1,5)

    #event handler now prints currently selected card from treeview
    def on_clicked(self):
        #Get the list of Qmodels within the treeview
        selectedIndex = self.selectedIndexes()

        #Initialize variables to store the items
        selectionList = []

        #For the number of Qmodels get the items
        for i in range(len(selectedIndex)):
            #track where the index is currently
            currentIndex = selectedIndex[i]
            #use the index to get the name, cost and image string from the selected item
            item = self.model.itemFromIndex(currentIndex)
            print(item.text())

            
        






            
            




